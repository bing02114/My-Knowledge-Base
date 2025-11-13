### **1. Introduction: From Value-Based to Policy-Based**

### **(1. 简介：从基于价值到基于策略)**

- **Previous Approach (Value-Based):** In weeks 1-5, we learned action-value functions ($Q(s,a)$) and then derived a policy from them (e.g., $\epsilon$-greedy)1111.
    
    - **(以前的方法 - 基于价值):** 在第1-5周，我们学习动作价值函数 ($Q(s,a)$)，然后从中推导出策略（例如 $\epsilon$-贪婪策略）。
        
- **New Approach (Policy-Based):** In Week 6, we learn the policy directly by parameterizing it2.
    
    - **(新方法 - 基于策略):** 在第6周，我们通过参数化直接学习策略。
        
- **Limitations of Value-Based Methods (e.g., $\epsilon$-greedy):**
    
    - **Abrupt Changes:** Small changes in Q-values can drastically switch the policy3.
        
        - **(突变):** Q值的微小变化可能导致策略的剧烈改变。
            
    - **No Stochastic Optimality:** They cannot represent optimal policies that require specific probabilities (e.g., Rock-Paper-Scissors requires 1/3 probability for each action) .
        
        - **(无随机最优性):** 它们无法表示需要特定概率的最优策略（例如，石头剪刀布需要每种动作 1/3 的概率）。
            
    - **Continuous Actions:** Calculating `argmax` over an infinite action space is difficult.
        
        - **(连续动作):** 在无限动作空间上计算 `argmax` 非常困难。
            

---

### **2. Policy Parameterization**

### **(2. 策略参数化)**

- **Definition:** A parameterized policy $\pi(a|s, \theta)$ defines the probability of taking action $a$ in state $s$, given parameters $\theta$ 6.
    
    - **(定义):** 参数化策略 $\pi(a|s, \theta)$ 定义了在给定参数 $\theta$ 的情况下，在状态 $s$ 采取动作 $a$ 的概率。
        
- **Discrete Actions (Softmax Policy):**
    
    - Uses action preferences $h(s,a,\theta)$.
        
    - Formula: $\pi(a|s,\theta) = \frac{e^{h(s,a,\theta)}}{\sum_{b}e^{h(s,b,\theta)}}$ .
        
    - **(离散动作 - Softmax策略):** 使用动作偏好 $h(s,a,\theta)$。公式如上。
        
- **Continuous Actions (Gaussian Policy):**
    
    - The policy outputs the mean $\mu$ and standard deviation $\sigma$ of a normal distribution.
        
    - Formula: $\pi(a|s,\theta) = \frac{1}{\sigma(s,\theta)\sqrt{2\pi}} \exp(-\frac{(a-\mu(s,\theta))^2}{2\sigma(s,\theta)^2})$.
        
    - Action selection involves sampling from this distribution: $a \sim \mathcal{N}(\mu, \sigma^2)$.
        
    - **(连续动作 - 高斯策略):** 策略输出正态分布的均值 $\mu$ 和标准差 $\sigma$。动作选择涉及从该分布中采样。
        
- **Optimization Goal:** Maximize a performance measure $J(\theta)$, typically the value of the start state $V_{\theta}^{\pi}(s_0)$ .
    
    - **(优化目标):** 最大化性能度量 $J(\theta)$，通常是起始状态的价值 $V_{\theta}^{\pi}(s_0)$。
        
    - **Method:** Gradient Ascent: $\theta_{t+1} = \theta_t + \alpha \nabla J(\theta_t)$.
        
    - **(方法):** 梯度上升。
        

---

### **3. The Policy Gradient Theorem**

### **(3. 策略梯度定理)**

- **The Challenge:** Calculating the gradient is hard because changing $\theta$ affects both the **action selection** and the **state distribution** (which depends on unknown environment dynamics) .
    
    - **(挑战):** 计算梯度很难，因为改变 $\theta$ 既影响**动作选择**，也影响**状态分布**（这取决于未知的环境动态）。
        
- **The Theorem:** The theorem provides a way to compute the gradient without knowing the environment's dynamics:
    
    - $\nabla J(\theta) \propto \sum_{s} \mu(s) \sum_{a} Q^{\pi}(s,a) \nabla \pi(a|s, \theta)$.
        
    - **(定理):** 该定理提供了一种在不知道环境动态的情况下计算梯度的方法（公式如上）。
        
- **The Log-Derivative Trick:** To make this practical for sampling, we convert the sum into an expectation using $\nabla \ln f = \frac{\nabla f}{f}$:
    
    - $\nabla J(\theta) \propto \mathbb{E}_{\pi} [Q^{\pi}(S_t, A_t) \nabla \ln \pi(A_t|S_t, \theta)]$.
        
    - **(对数导数技巧):** 为了使其适用于采样，我们利用 $\nabla \ln f = \frac{\nabla f}{f}$ 将求和转换为期望。
        
- **Interpretation:**
    
    - $\nabla \ln \pi$: The **Score Function** or Eligibility Vector. Points in the direction that makes the action more likely.
        
    - $Q^{\pi}$: The weight. If $Q$ is high, we move strongly in that direction.
        
    - **(解释):** $\nabla \ln \pi$ 是**得分函数**或资格向量。指向使动作概率增加的方向。$Q^{\pi}$ 是权重。如果 $Q$ 很高，我们就向那个方向大幅移动。
        

---

### **4. REINFORCE Algorithm**

### **(4. REINFORCE 算法)**

- **Monte Carlo Policy Gradient:** Since we don't know true $Q^{\pi}$, REINFORCE uses the actual sample return $G_t$ as an unbiased estimate.
    
    - **(蒙特卡洛策略梯度):** 由于不知道真实的 $Q^{\pi}$，REINFORCE 使用实际样本回报 $G_t$ 作为无偏估计。
        
- **Update Rule:** $\theta_{t+1} = \theta_t + \alpha G_t \nabla \ln \pi(A_t|S_t, \theta_t)$.
    
    - **(更新规则):** 公式如上。如果 $G_t$ 为正，增加该动作的概率；如果为负，减少该概率。
        
- **Issue:** High Variance. Returns $G_t$ vary greatly between episodes, making learning slow and unstable.
    
    - **(问题):** 高方差。回报 $G_t$ 在不同回合间变化很大，导致学习缓慢且不稳定。
        
- **Solution (Baseline):** Subtract a baseline $b(s)$ from the return to reduce variance without introducing bias.
    
    - **Update:** $\theta_{t+1} = \theta_t + \alpha [G_t - b(S_t)] \nabla \ln \pi(A_t|S_t, \theta_t)$.
        
    - **Common Baseline:** The learned state-value function $\hat{V}(s, w)$. The term $[G_t - \hat{V}(S_t)]$ represents how much better an action was compared to the average.
        
    - **(解决方案 - 基线):** 从回报中减去基线 $b(s)$ 以降低方差且不引入偏差。通常使用学习到的状态价值函数 $\hat{V}(s, w)$ 作为基线。$[G_t - \hat{V}(S_t)]$ 项表示该动作比平均水平好多少。
        

---

### **5. Actor-Critic Methods**

### **(5. Actor-Critic 方法)**

- **Concept:** Combine Policy Gradient (Actor) with TD Learning (Critic) to get low variance and online updates.
    
    - **(概念):** 结合策略梯度（演员）和时序差分学习（评论家），以获得低方差和在线更新。
        
- **Mechanism:** Replace the Monte Carlo return $G_t$ with a one-step TD target $R_{t+1} + \gamma \hat{V}(S_{t+1})$.
    
    - **(机制):** 用单步 TD 目标 $R_{t+1} + \gamma \hat{V}(S_{t+1})$ 替换蒙特卡洛回报 $G_t$。
        
- **Components:**
    
    - **Critic (Value):** Updates parameters $w$ to minimize TD error $\delta_t$.
        
    - **Actor (Policy):** Updates parameters $\theta$ using the TD error as the signal: $\theta_{t+1} = \theta_t + \alpha \delta_t \nabla \ln \pi$.
        
    - **(组件):** **评论家**更新参数 $w$ 以最小化 TD 误差；**演员**使用 TD 误差作为信号更新参数 $\theta$。
        

---

### **6. Deep RL & Modern Methods (Overview)**

### **(6. 深度强化学习与现代方法概览)**

- **Problem with Vanilla PG:** Choosing step size $\alpha$ is hard. Too large leads to "catastrophic policy collapse" .
    
    - **(原始 PG 的问题):** 选择步长 $\alpha$ 很难。太大导致“灾难性策略崩溃”。
        
- **TRPO (Trust Region Policy Optimization):** Constraints the update so the new policy doesn't differ too much from the old one (using KL divergence) .
    
    - **(TRPO):** 约束更新，使新策略与旧策略差异不太大（使用 KL 散度）。
        
- **PPO (Proximal Policy Optimization):** Simpler than TRPO. Uses a "clipped" objective to prevent the probability ratio $r_t(\theta)$ from changing too much .
    
    - **(PPO):** 比 TRPO 简单。使用“截断”目标函数来防止概率比率 $r_t(\theta)$ 变化过大。
        
- **DPG/DDPG (Deterministic Policy Gradients):**
    
    - Used for high-dimensional continuous action spaces where sampling is inefficient .
        
    - Learns a deterministic policy $a = \mu_{\theta}(s)$.
        
    - Uses **Off-policy** learning (Exploration via noise in behavior policy, Exploitation in target policy) .
        
    - **(DPG/DDPG):** 用于采样效率低下的高维连续动作空间。学习确定性策略 $a = \mu_{\theta}(s)$。使用**异策略**学习（通过行为策略中的噪声进行探索，在目标策略中进行利用）。