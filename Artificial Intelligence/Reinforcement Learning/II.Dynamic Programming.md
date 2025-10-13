### 1.Introduction

#### 1.1 Definition

>A method for solving complex problems by breaking them down into simpler subproblems, solving each subproblem once, and storing the results

### 2.Policy Evaluation

#### 2.1 Algorithm

Turn the Bellman equation into an update rule:

**Iterative Policy Evaluation**

1. Initialize $V_0(s)=0$ for all s (or any arbitary values)
2. For k = 1,2,3 ... :

$$V_{k+1}(s)=\sum_{a}\pi (a|s)\sum_{s',r}P(s',r|s,a)[r+\gamma V_{k}(s')]$$

3. Stop when $max_s|V_{k+1}(s)-V_{k}(s)|<\theta$

#### 2.2 Implementation Strategies

**Jacobi: Synchronous Updates**

* Use $V_{k}(s')$ for all next states
* <font color="red">Update all states simultaneously</font>
* Requires two arrays: old and new values

$$V_{new}(s)\leftarrow \sum_{a}\pi(a|s)\sum_{s',r}P(s',r|s,a)[r+\gamma V_{old}(s')]$$

**Gauss-Seidel: In-Place Updates**

* Use most recent values available
* <font color="Red">Update states one at a time</font>
* Can use single array, often converges faster

$$V(s)\leftarrow \sum_{a}\pi(a|s)\sum_{s',r}P(s',r|s,a)[r+\gamma V(s')]$$

### 3.Policy Improvement

#### 3.1 Greedy Policy Improvement


$$\pi'(s)=argmax_{a}Q_{\pi}(s,a)$$

#### 3.2 Prove this theorem

Assumption:

$$V^{\pi} \leq Q_{\pi}(s,\pi'(s))$$

Q-function def:

$$=E[R_{t+1}+\gamma V^{\pi}(S_{t+1})|S_t=s,A_t=\pi'(s)]$$

Expectation under $\pi'$:

$$=E_{\pi'}[R_{t+1}+\gamma V^{\pi}(S_{t+1})|S_t=s]$$

Apply assumption again:

$$\leq E_{\pi'}[R_{t+1}+\gamma Q_{\pi}(S_{t+1},\pi')|S_t=s]$$

Expand Q:

$$=E_{\pi'}[R_{t+1}+\gamma E[R_{t+2}+\gamma V^{\pi}(S_{t+2})|S_{t+1},A_{t+1}=\pi'(S_{t+1})]|S_t=s]$$

Combine Expectations:

$$=E_{\pi'}[R_{t+1}+\gamma R_{t+2}+\gamma^2R_{t+3}|S_t=s]$$

Repeat:

$$\leq E_{\pi'}[R_{t+1}+\gamma R_{t+2}+\gamma^2R_{t+3}+\gamma^3R_{t+4}+\dots|S_t=s]$$

Definition of $V_{\pi'}$

$$=V_{\pi'}(s)$$

### 4.Policy Iteration

#### 4.1 Definition

>Combine evaluation and improvement

#### 4.2 Algorithm

1. **Initalize**: Arbitary policy $\pi_0$
2. **Repeat Until Convergence:**

* Policy Evaluation: Compute $V^{\pi}_k$ using iterative evaluation
* Policy Improvement: Set $\pi_{k+1}(s)=\arg\max_{a}Q_{\pi_{k}}(s,a)$

3. Stop when $\pi_{k+1}=\pi_{k}$

#### 4.3 Optimality

**Property 1: Monotonic Improvement**

>Each iteration either strictly improves the policy or the policy is already optimal

**Property 2: Finite Convergence**

* Finite number of possible policies: $|A|^{|S|}$
* Each improvement is strict
* Must reach optimal policy in finite steps

### 5.Value Iteration

#### 5.1 Ineffciency in Policy Iteration

**Policy Evaluation: Run iterative evaluation until convergence**

**The computational waste**

* Policy evaluation might take 100+ iterations to converge
* We immediately throw away this policy after improvement
* Early iterations of evaluation give us the ”general shape” of values
* Perfect accuracy isn’t needed if we’re changing the policy anyway

#### 5.2 Value Iteration

1. Initialize $V_{0}(s)=0$ for all s
2. For k=1,2,3...:

$$V_{k+1}(s)=max_{a}\sum_{s',r}P(s',r|s,a)[r+\gamma V_{k}(s')]$$ for all s

3. Stop when $max_{s}|V_{k+1}(s)-V_{k}(s)|<0$
4. Extract policy $\pi^{*}(s)=\arg\max_{a}\sum_{s',r}P(s',r|s,a)[r+\gamma V^{*}(s')]$

**Key difference from Policy Evaluation**

>The max operator instead of weighted sum over policy


### 6. Generalized Policy Iteration
#### 6.1 Definition

>The general idea of letting policy evaluation and policy improvement
>processes interact, independent of the granularity and other details.

**GPI Pattern**

* **Evaluation**: Make value function consistent with current policy
* **Improvement**: Make policy greedy with respect to current value function
* These processes work toward the same goal from different directions

**GPI Spectrum**

* **Policy Iteration**: Complete evaluation, then improvement
* **Value Iteration**: One-step evaluation, then improvement
* **Asynchronous DP**: Update states individually, any order

#### 6.2 Asynchronous Dynamic Programming

**Key Insight**

>We don’t need to update all states in each iteration - we can focus
>computation where it matters most.

**Asynchronous Strategies**

* Random: Pick states uniformly at random
* Prioritized: Update states with largest value changes first
* Real-time: Update states along simulated trajectories

**Convergence Guarantee**

>Still works if all states updated infinitely often

#### 6.3 Limitations of DP

**Three Fundamental Limitations**

* Perfect Model Required: Need exact P(s′|s, a) and R(s, a, s′)
* Computational Complexity: Must iterate over all states and actions
* Curse of Dimensionality: State space grows exponentially as |S| and |A| increases

**Real-World Challenges**

* Robotics: Need perfect physics simulation
* Finance: Need perfect market model
* Games: Environment rules might be unknown