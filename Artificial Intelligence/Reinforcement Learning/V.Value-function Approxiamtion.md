### 1.Introduction: Why We Need Approximation
#### 1.1 The Problem with Tabular Methods

* Tabular methods learn an exact value for each state
* This fails in real-world scenarios dut to the **Scale Problem**
* State spaces are often too large or continuous / infinite
* We cannot store a table with too many entries, nor can we visit every state to learn its value

#### 1.2 The Solution: Value Function Approximation (VFA)

**Core Idea**

>Instead of a table, we represent the value function as a parameterized function

$$\hat{V}(s,\theta)≈V^{\pi}(s)$$

**Parameters**

>$\theta$ : This is a parameter vector

**Tractability**

>The number of parameters (d) is _much smaller_ than the number of states (d≪∣S∣)

**Learning**

>Learning becomes an optimization problem: we adjust θ to make our approximation V^(s,θ) closer to the true value Vπ(s).

**Generalization**

>This is the key benefit. When we update θ based on one state, it affects the values of many other similar states

***
### 2.Stochastic Gradient Descent (SGD)

#### 2.1 The Goal

* We want to find parameters $\theta$ that minimize the expected squared error between our approximation $\hat{V}$ and the true value $V^{\pi}$
* Ideal Update

$$\theta_{t+1}=\theta_{t}-\frac{1}{2}\alpha\nabla_{\theta}E[(V_{\pi}(S_t)-\hat{V}(S_t,\theta_t))^{2}]$$

#### 2.2 The Two Problem

1. We don't know the true value $V_{\pi}(S_t)$
2. We can't compute the full expectation E

#### 2.3 The Two Solutions

1. Replace the unknown true value $V_{\pi}(S_t)$ with a target estimate $U_t$
2. Replace the full expectation with a single sample from the current time step $S_t$. This is **Stochastic Gradient Descent (SGD)**

#### 2.4 The General SGD Update Value

1. start:

$$\theta_{t+1}=\theta_{t}-\frac{1}{2}\alpha\nabla_{\theta}[(U_t-\hat{V}(S_t,\theta_t))^{2}]$$

2. Apply Chain Rule

$$\nabla_{\theta}=-2(U_t-\hat{V}(S_t,\theta_t))\nabla_{\theta}\hat{V}(S_t,\theta_t)$$

3. Combine

$$\theta_{t+1}=\theta_{t}+\alpha[U_t-\hat{V}(S_t,\theta_t)]\nabla_{\theta}\hat{V}(S_t,\theta_t)$$


#### 2.5 Targets for Different RL Methods

**Monte Carlo**

$$U_t=G_t$$

**TD(0)**

$$U_t=R_{t+1}+\gamma\hat{V}(S_{t+1},\theta_t)$$

#### 2.6 Semi-Gradient

* The TD(0) update is called a "semi-gradient" method.
* This is because the target Ut​=Rt+1​+γV^(St+1​,θt​) itself depends on the parameters θt​
* A "full" gradient would be complex and unstable. We "cheat" by **treating the target as a fixed number**, which is simpler, cheaper, and more stable.

***
### 3.Linear Function Approximation

#### 3.1 Definition

* First, we must define a **feature vector** x(s)=(ϕ1​(s),...,ϕd​(s))T. This represents the state s (e.g., agent's position, velocity, etc.).
* The value function is a simple linear combination (dot product) of the parameters and features: V^(s,θ)=θTx(s).

#### 3.2 Key Properties

>The approximation is linear in the _parameters_ θ, but it can be nonlinear in the _state_ s if the features ϕi​(s) are complex

#### 3.3 Advantages

>The gradient is very simple: $\nabla_{\theta}(s,\theta)=x(s)$

* This simplifies the SGD update to:

$$\theta_{t+1}=\theta_{t}+\alpha[U_t-\theta^{T}_{t}x(S_t)]x(S_t)$$
* It also has strong convergence guarantees (it has one global optimum).

#### 3.4 Feature Construction

* The success of linear methods depends _critically_ on hand-crafting good features
* **Polynomial Features (多项式特征):** Model interactions between state variables (e.g., x1​,x2​,x1​x2​,x12​,...). Disadvantage: The number of features grows exponentially.
* **Tile Coding (分块编码):** Divides the state space into multiple _overlapping_ grids (tilings). A state is represented by a binary vector indicating which tiles it falls into. This allows good generalization between nearby states.
* **Radial Basis Functions (RBFs) (径向基函数):** A continuous generalization of tile coding. Features are Gaussian "bumps" centered at ci​, and their value ϕi​(s) decreases as the state s moves away from the center.
***
### 4.Nonlinear Function Approximation: Artificial Neural Networks (ANNs)

#### 4.1 When Linear Fails

>Linear methods fail when we can't hand-craft good features, such as from raw sensory data (like images) or in very high-dimensional spaces.

#### 4.2 ANNs as a Solution

* ANNs are **universal function approximators** (they can represent any continuous function).
* Their key capability is **automatic feature learning** in their hidden layers

#### 4.3 How They Work

* They are built from basic units called **neurons** (or perceptrons): y=f(wTx+b)
* The **Activation Function** f(⋅) (e.g., **ReLU** max(0,z)) is what introduces non-linearity.
* Without activation functions, a deep network just collapses into a single linear function.

#### 4.4 Learning

* They learn using **Backpropagation**, which is a high-level algorithm that uses the chain rule to compute the error gradient for all parameters (weights and biases) in the network.
***
### 5.Deep Reinforcement Learning (DRL)

#### 5.1 Deep Q-Networks (DQN)

**Goal**

>To solve complex tasks (like Atari games) from raw pixel inputs (84×84×4 images)

**Architecture**

>A Convolutional Neural Network (CNN) that takes the _state_ (image) as input and outputs a _Q-value for each discrete action_.

**Key Innovations for Stability**

**1.Experience Replay**

* **Problem:** Sequential states are highly correlated, which violates the i.i.d. (Independent and Identically Distributed) assumption of SGD.
* **Solution:** Store transitions (st​,at​,rt​,st+1​) in a large **replay buffer** D. Instead of learning from the last transition, the algorithm samples a _random mini-batch_ of transitions from D to perform updates.
* **Benefit:** Breaks temporal correlations and allows for repeated learning from the same experience.

**2.Target Networks**

* **Problem:** The Q-learning target r+γ maxa​Q(st+1​,a) is a "moving target" because it is computed using the same network that is being updated.
* **Solution:** Use a _separate_ **target network** Q(⋅;θ−) (with frozen parameters) to compute the target: Target=r+γ maxa​Q(st+1​,⋅;θ−).
* **Update Rule:** The target network's weights θ− are only updated periodically (e.g., every C steps) by copying the main network's weights θ (θ−←θ). This keeps the target stable.

**3.Reward Clipping**

* Clips all rewards to the range [−1,+1] to stabilize learning across games with different reward scales.

#### 5.2 Coarse-to-fine Q-Networks (CQN)

* **Problem (问题):** How to apply DQN to **continuous action spaces** (e.g., robotics)?
* **Naive Solution Failure (朴素解法的失败):** Simply discretizing each action dimension (e.g., 7 robot joints) leads to an _exponential_ explosion of possible actions (1007=1014 actions), which is impossible to learn.
* **CQN Insight (CQN 的见解):** Instead of one fine-grained discretization, use a **hierarchical discretization** (分层离散化).

**Approach**

* Start with a _coarse_ discretization (e.g., 3 large bins).
* Use a Q-network to select the best coarse _interval_.
* **"Zoom in"** (放大) on that selected interval and discretize it _again_ (e.g., into 3 finer bins).
* Repeat this process for L levels. This allows high precision with only B×L actions to evaluate, instead of BL.
