### 1.Introduction: Value-Based vs. Policy-Based

**Value-Based Methods**

* These methods learn an action-value function, Q(s,a).
* A policy is then derived from these values, typically using an ϵ-greedy strategy.

**Policy-Based Methods**

* These methods learn the policy π(a∣s,θ) directly, by parameterizing it with θ.
* They optimize the parameters θ directly instead of consulting a value function to select actions.

**Limitations of Value-Based Methods**

* **Continuous Actions (连续动作):** They cannot handle continuous action spaces because it is impossible to perform an `argmax` over an infinite number of actions.
* **Stochastic Policies (随机策略):** An ϵ-greedy policy cannot represent all possible stochastic policies. For example, in Rock-Paper-Scissors, the optimal policy is to play each action with 1/3 probability, which ϵ-greedy cannot achieve.

***
### 2.Policy Parameterization

**Core Idea**

>We define the policy as a differentiable function π(a∣s,θ) with parameters θ.

**For Discrete Action: Softmax Policy**

* We estimate "action preferences" h(s,a,θ) for each action.
* The Softmax function converts these preferences (which can be any real number) into a valid probability distribution.
* **Formula (公式):**

$$\pi(a|s,\theta)=\frac{e^{h(s,a,\theta)}}{\sum_b e^{h(s,b,\theta)}}$$

**For Continuous Actions: Gaussian Policy**

* The policy learns the parameters for a probability distribution (e.g., a Gaussian distribution).
* The parameters θ define the **mean (均值) μ(s,θ)** and **standard deviation (标准差) σ(s,θ)**.
* An action is then sampled from this distribution: a∼N(μ(s,θ),σ(s,θ)2).

**Optimization Goal**

* We need a performance measure J(θ) to optimize.
* For episodic tasks, this is the value of the start state: J(θ)=Vθπ​(s0​).
* We use **gradient ascent** to find the θ that maximizes this performance.
* **Update Rule (更新规则):** θt+1​=θt​+α∇J(θt​).

**The Challenge**

* How to compute the gradient ∇J(θ)? The performance J(θ) depends on both the action selection (which we can differentiate) and the state distribution (which depends on the unknown environment dynamics) .

***
### 3.The Policy Gradient Theorem

**The Main Result**

>This theorem provides a way to compute the gradient ∇J(θ) without needing to know or differentiate the environment's dynamics (i.e., the state distribution).

**Theorem**

$$\nabla J(\theta)∝ \sum_s \mu(s)\sum_a Q^{\pi}(s,a)\nabla_{\pi}(a|s,\theta)$$

**The "Log-Derivative Trick"**

$$\frac{\nabla_{\pi}}{\pi}=\nabla \ln \pi$$

$$\nabla J(\theta)=E_{\pi}[Q^{\pi}(S_t,A_t)\nabla\ln \pi(A_t|S_t,\theta)]$$

**Interpretation**

* **∇lnπ(At​∣St​,θ):** This is the **"score function"** or **"eligibility vector"**. It's a vector that points in the direction in parameter space (θ) that most increases the probability of the action At​ that was just taken.
* **Qπ(St​,At​):** This term "weights" that direction. If Qπ (the value of that action) is high, we push θ significantly in that direction. If it's low, we push less (or in the opposite direction).

***
### 4.REINFORCE: Monte Carlo Policy Gradient

