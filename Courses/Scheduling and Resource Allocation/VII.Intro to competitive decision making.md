### 1.What is Game Theory

#### 1.1 Popular Perception

>Formal games like Chess, Go, or Poker

#### 1.2 Concrete Snapshot

>It's the mathematical framework for analyzing or designing any multi-agent decision-making system.

***
### 2.The Primitives of a Game (The Formal Definition)

**A formal game is defined by three key ingredients:**

1. **Players**: A set of $N$ players, indexed $i = 1, ..., N$
2. **Actions**: Each player $i$ has a set of possible actions they can take, $\mathcal{X}_i$. An "outcome" of the game is a vector of actions, one from each player: $(x_1, x_2, ..., x_N)$.
3. **Costs**: Each player $i$ has a **cost function** $J_i(x_1, ..., x_N)$ that depends on the actions of _all_ players

#### 2.1 Bi-Matrix Representation

**For a two-player game, we can represent all outcomes in a simple matrix**

- Player 1 is the "Row Player". (参与者1是“行玩家”。)
    
- Player 2 is the "Column Player". (参与者2是“列玩家”。)
    
- Each cell contains the costs: `(Cost for Player 1, Cost for Player 2)`. (每个单元格包含成本：`(参与者1的成本, 参与者2的成本)`。)

***
### 3.Pure Nash Equilibrium (PNE)

#### 3.1 Definition

>A Pure Nash Equilibrium (PNE) is a set of actions (an outcome) where no single player can get a _better_ result (a lower cost) by **unilaterally deviating** (changing only their own action).

#### 3.2 Formal Definition

$$J_i(x_i^*, x_{-i}^*) \le J_i(x_i, x_{-i}^*), \quad \forall x_i \in \mathcal{X}_i$$

- $x_i^*$ is the player's chosen action. (是该参与者选择的行动。)
    
- $x_{-i}^*$ represents the actions of _everyone else_. (代表_其他所有人_的行动。)
    
- This formula says: "My cost for playing my equilibrium action $x_i^*$ is less than or equal to my cost for playing any _other_ action $x_i$, assuming everyone else sticks to their plan $x_{-i}^*$." (这个公式是说：“假设其他所有人都坚持他们的均衡行动 $x_{-i}^*$，我玩我的均衡行动 $x_i^*$ 所付出的成本，小于或等于我玩任何_其他_行动 $x_i$ 所付出的成本。”)

***
### 4.Best-Response Algorithm

>This is an algorithm used to _find_ a Pure Nash Equilibrium.

#### 4.1 Defintion

>A player $i$'s "Best Response" is the action $x_i$ that minimizes their cost, given what everyone else ($x_{-i}$) is doing.


$$BR(x_{-i}) = \arg\min_{x_i \in \mathcal{X}_i} J_i(x_i, x_{-i})$$

#### 4.2 Algorithm

1. Initialize with any random set of actions $x$. (从任意一组随机行动 $x$ 开始。)
    
2. Iterate through the players $i = 1, 2, ..., N, 1, 2, ...$ (轮流遍历所有参与者 $i = 1, 2, ..., N, 1, 2, ...$)
    
3. For the current player $i$, update their action to their Best Response: (对于当前参与者 $i$，将其行动更新为他们的最佳响应：) $x_i \leftarrow BR(x_{-i})$
    
4. If no player changes their action (the system is stable), a PNE has been found. Stop. (如果没有参与者改变他们的行动 (系统稳定了)，就找到了一个 PNE。停止。)
    

- **Question:** If this algorithm converges, what does it converge to? (问题：如果这个算法收敛了，它收敛到什么？)
    
- **Answer:** A Pure Nash Equilibrium. (答案：一个纯纳什均衡。)
    
- **Question:** Does it _always_ converge? (问题：它_总是_会收敛吗？)
    
- **Answer:** No. (This motivates the need for Mixed Equilibria). (答案：不是。(这激发了对混合均衡的需求)。)

***
### 5.Mixed Nash Equilibrium (MNE)

#### 5.1 Problem

>Some games, like "Matching Pennies" (猜硬币正反), have **no Pure Nash Equilibrium**. The Best-Response algorithm would loop forever

#### 5.2 Idea

>Instead of _deterministically_ choosing one action, players can **randomize** their decision by choosing a probability distribution $\sigma_i$ over their actions

**Goal**

>Players now aim to minimize their **Expected Cost** $C_i(\sigma_1, ..., \sigma_N) = \mathbb{E}_{x \sim \sigma}[J_i(x)]$

#### 5.3 Definition

>A set of probability distributions $(\sigma_1^*, ..., \sigma_N^*)$ is an MNE if no player can decrease their expected cost by deviating to any other strategy (including any single _pure_ strategy)