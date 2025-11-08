### 1.Potential Games (PG)

#### 1.1 Definition

>A game is a **Potential Game (势博弈)** if there exists a single global function $\Phi$ (the "potential function") that perfectly mirrors the change in any single player's cost

$$\underbrace{J_i(x_i, x_{-i}) - J_i(y_i, x_{-i})}_{\text{Change in Player } i\text{'s cost (参与者}i\text{的成本变化)}} = \underbrace{\Phi(x_i, x_{-i}) - \Phi(y_i, x_{-i})}_{\text{Change in Global Potential (全局势能的变化)}}$$

**Intuition**

>This means that if a player $i$ selfishly makes a move that _lowers_ their _own cost_ (e.g., $J_i$ decreases by 10), the global potential $\Phi$ _must_ also decrease by the exact same amount (by 10).
>
>This aligns every player's self-interest with the "global interest" of minimizing $\Phi$.

***
### 2.Properties of Potential Games

1. **A Pure Nash Equilibrium (PNE) Always Exists.** (纯纳什均衡 (PNE) 总是存在。)
    
2. **The Best-Response (BR) Algorithm Always Converges.** (最佳响应 (BR) 算法总是收敛。)

#### 2.1 Proof

- The proof for convergence is elegant: (收敛性的证明非常巧妙：)
    
- Assume the BR-algorithm _does not_ terminate. Since there are a finite number of states, it must eventually enter a cycle (e.g., $x^1 \to x^2 \to \dots \to x^k \to x^1$). (假设 BR 算法_不_终止。由于只有有限个状态，它最终必须进入一个循环 (例如 $x^1 \to x^2 \to \dots \to x^k \to x^1$)。)
    
- Each step in a BR-algorithm is a selfish move that _decreases_ the player's cost ($J_i$ goes down). (BR 算法中的每一步都是一个自利的行动，它_降低_了该参与者的成本 ($J_i$ 下降)。)
    
- Because it's a potential game, every time $J_i$ decreases, $\Phi$ _must also decrease_. (因为这是一个势博弈，每当 $J_i$ 下降时，$\Phi$ _也必须下降_。)
    
- This would imply: $\Phi(x^1) > \Phi(x^2) > \dots > \Phi(x^k) > \Phi(x^1)$.
    
- This is a contradiction ($\Phi(x^1) > \Phi(x^1)$ is impossible). (这是一个矛盾 ($\Phi(x^1) > \Phi(x^1)$ 是不可能的)。)
    
- Therefore, the algorithm cannot cycle and must terminate. Since it only terminates when no player can make a best-response move, it _must_ terminate at a **Pure Nash Equilibrium**. (因此，该算法不能循环，必须终止。由于它只在没有参与者能做出最佳响应时才终止，所以它_必须_在一个**纯纳什均衡**处终止。)

***
### 3.Congestion Games (CG)

#### 3.1 Definition

1. **A set of Players** $N = \{1, ..., N\}$ (e.g., drivers). (一组**参与者** $N = \{1, ..., N\}$ (例如，司机)。)
    
2. **A set of Resources** $\mathcal{R}$ (e.g., roads). (一组**资源** $\mathcal{R}$ (例如，道路)。)
    
3. **Player Actions (行动):** Each player $i$ chooses an **action** $x_i$, which is a **subset of resources** (e.g., a path, which is a set of roads). (每个参与者 $i$ 选择一个**行动** $x_i$，这个行动是一个**资源的子集** (例如，一条路径，它是一组道路的集合)。)
    
4. **Cost Functions (成本函数):** Each _resource_ $r$ has a cost function $l_r(k)$ that depends on $k$, the _number of players_ using that resource. (每个_资源_ $r$ 都有一个成本函数 $l_r(k)$，它取决于 $k$，即_使用该资源的参与者数量_。)
    
5. **Player Cost (参与者成本):** A player's total cost is the **sum of the costs** of all resources they chose. (一个参与者的总成本是他们所选择的所有资源的**成本总和**。)
    
    - $|x|_r$ = total number of players using resource $r$. (使用资源 $r$ 的总参与者数。)
        
    - $J_i(x) = \sum_{r \in x_i} l_r(|x|_r)$

#### 3.2 Example

- **Players (参与者)** = Tasks (e.g., $n$ compute jobs). (任务 (例如 $n$ 个计算作业))
    
- **Resources (资源)** = Machines (e.g., $m$ servers). (机器 (例如 $m$ 台服务器))
    
- **Action (行动)** = Each task $i$ chooses _one_ machine $r$ to run on. ($x_i = \{r\}$). (每个任务 $i$ 选择_一台_机器 $r$ 来运行。($x_i = \{r\}$))
    
- **Cost (成本)** = The runtime (cost) of the chosen machine, $l_r(|x|_r)$, which increases with the number of tasks on it. (所选机器的运行时间 (成本)，$l_r(|x|_r)$，它随着机器上的任务数量增加而增加。)

***
### 4.Congestion Games are Potential Games

#### 4.1 Theorem

>_Every_ congestion game is a potential game

#### 4.2  **The Potential Function (势函数):** 

The lecture defines a specific potential function, known as the **Rosenthal Potential Function**

$$\Phi(x) = \sum_{r \in \mathcal{R}} \sum_{j=1}^{|x|_r} l_r(j)$$

- **What this means (其含义):** The global potential is the sum, over all resources, of the "cost for the 1st person to use this resource" + "cost for the 2nd person" + ... + "cost for the $k$-th person". (这个全局的势函数是，对所有资源求和，(“第1个使用该资源的参与者的成本” + “第2个参与者的成本” + ... + “第 $k$ 个参与者的成本”)。)
    
- The slides show a proof that when any player $i$ unilaterally switches their action, the change in their personal cost $J_i$ is _exactly equal_ to the change in this global potential $\Phi$. (幻灯片展示了一个证明：当任何参与者 $i$ 单方面改变其行动时，其个人成本 $J_i$ 的变化_完全等于_这个全局势函数 $\Phi$ 的变化。)

#### 4.3 Implication

>Because all congestion games are potential games, we now know that **all congestion games have a Pure Nash Equilibrium**, and the **Best-Response (BR) algorithm is guaranteed to find one**.

***
### 5.Convergence Speed

- **Question (问题):** We know the BR algorithm converges, but how _fast_? (我们知道 BR 算法会收敛，但_多快_呢？)
    
- **General Case (一般情况):** In some complex (non-singleton) congestion games, it can take an exponential number of steps. (在某些复杂的 (非单一) 拥塞博弈中，可能需要指数级的步数。)
    
- **Singleton Congestion Games (单一拥塞博弈):**
    
    - **Definition (定义):** A special case where every player's action $x_i$ consists of choosing _exactly one_ resource. (e.g., the Load Balancing game). (一个特殊的例子，其中每个参与者的行动 $x_i$ 都只包含选择_恰好一个_资源。(例如负载均衡博弈)。)
        
    - **Theorem (定理):** In singleton congestion games, the Best-Response algorithm converges **quickly** (in polynomial time, $O(n^{2}m)$ steps). (在单一拥塞博弈中，最佳响应算法收敛得**非常快** (在多项式时间，$O(n^{2}m)$ 步内)。)
        
    - **Proof Idea (证明思路):** You can create new _integer-based_ costs that preserve the players' preferences. The total potential $\Phi$ is then bounded by $n^2m$. Since every BR step is an improvement, $\Phi$ must decrease by at least 1 each time. Therefore, the algorithm must terminate in at most $n^2m$ steps. (您可以创建新的_基于整数_的成本，同时保持参与者的偏好不变。此时，总势函数 $\Phi$ 的上界为 $n^2m$
