### 1. The Formal Framework - Markov Decision Processes (MDPs)
#### 1.1 Formal Definition

>A model for sequential decision making when outcomes are uncertain.
>Formally defined by the tuple (S,A,R,P)

>S: Set of **states** - all possible situations
>A: Set of **actions** - all possible decisions
>R(s,a,s'): **Reward function** - immediate feedback for transitions
>P(s'|s,a): **Transition probabilities** - how actions change states

#### 1.2 The Markov Property

>The future is independent of the past, given the present.
><font color="Red">The next state only denpends on the current state and action, not the entire history</font>

#### 1.3 The Agent-Environment Interaction Loop

![](../Reinforcement%20Learning/images/interaction%20loop.png)
#### 1.4 Types of MDPs

> 1. Episodic: Tasks with a clear start and a terminal state, forming an "episode"
> 	1. game of chess
> 2. Continuing: Tasks that have no terminal states and go on indefinitely
> 	1. Stock trading

***
### 2. The Agent's Goal and Strategy
#### 2.1 The Policy
##### 1. Environment Dynamics: The State Transition Probability
$$P(s'|s,a) = P[S_{t+1}=s' | S_t=s, A_t=a]
$$
>The probability of transitoning to state's given current state s and action a

**Key Properties:**

>* Probability distribution: $$\sum_{s'\in S}P(s'|s,a)=1~for~all~s,a$$
>* Stationary: Transition probabilities don' change over time
>* Markovian: Next state depends only on current state and action

##### 2. The Agent's Behavior: The Policy

><font color="Red">A policy is the agent's stratrgy, which maps states to actions</font>

**Classification:**

>Deterministic: $$a = \pi(s)$$
>Stochastic: 
>$$a\sim \pi(a|s)$$

**Goal**

>To find the optimal policy, $$\pi^*$$
#### 2.2 The Return

**Discounted Return**

>To ensure returns are finite and to model a preference for immediate rewards, we use discounting

**Formula**

>$$G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} +~...~ = \sum^{∞}_{k=0}\gamma^k R_{t+k+1}$$

**Discount** **Factor**

>* A value between 0 and 1. 
>* If γ=0, the agent is "myopic" and only cares about immediate rewards; 
>* If γ=0.9, the agent is "balanced"
>* if γ is near 1, it is "far-sighted".

***
### 3. Evaluating the Strategy - Value Funcitons
#### 3.1 Core Idea

>* A value function predicts the <font color="Red">expected future reward</font> from a given state of state-action pair.
>* It tells us which states are "good" to be in.

#### 3.2 State-Value Function

>How good to be in state s
>$$V^{\pi}(s)=E[G_t|s_t=s,\pi]$$

#### 3.3 Action-Value Function

>How good is it to take action a in state s
>$$Q^{\pi}(s,a)=E[G_t|s_t=s,a_t=a,\pi]$$

***
### 4. Finding the Solution - Bellman Equations

#### 4.1 The Recursive Relationship

><font color="Red">The value of a state can be defined in terms of the values of its successor states. </font>
><font color="Red">This is the foundation for all RL algorithms</font>
#### 4.2 Bellman Equation for a Policy

**for State Values**

![](../Reinforcement%20Learning/images/BellmanEquationV.png)
>$$1.[r+\gamma V^{\pi}(s')]$$  `immediate reward r + the discounted value of the next state
>$$2.\sum_{s',r}P(s',r|s,a)[r+\gamma V^{\pi}(s')]$$  `This is action-value function`
>$$3.\sum_a\pi(a|s)$$  `Average over all possible actions the agent might take
>
>**The equation says**:
> <font color="red">The value of a state `s` under policy `\pi` is the weighted average of the values of all actions you might take from `s`, where the weights are the probabilities of taking each action according to `\pi`</font>

**for Action Values**

![](../Reinforcement%20Learning/images/BellmanEquationQ.png)

#### 4.3 Optimal Value Functions

>$$V^{*}(s)=max_{\pi}V^{\pi}(s)$$$$Q^{*}(s,a)=max_{\pi}Q^{\pi}(s,a)$$

**Relationship Between Optimal Functions**

>$$V^{*}(s)=max_aQ^*(s,a)$$

**Definition of Optimal Policy**

>$$\pi^{*}(s)=argmax_a~Q^*(s,a)$$
#### 4.4 Bellman Optimality Equations

**for State Values**

![](../Reinforcement%20Learning/images/BellmanOptimalityEquationsV.png)

**for Action Values**

![](../Reinforcement%20Learning/images/BellmanOptimalityEquationsQ.png)