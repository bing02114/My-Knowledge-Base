
### 1.MDP Formulation

#### 1.1 State and Action Spaces

State Spaces:

> the position of this robot
>
> S: {0,1,2,3,4}

Action Space:

> All the actions the robot can take
>
> A:{LEFT, RIGHT, STAY}

#### 1.2 Transition

**P(s'|s,a)** 

P(4|3,LEFT)=0

P(2|3,LEFT)=1

P(0|4,RIGHT)=0

P(4|3,RIGHT)=1

#### 1.3 Reward Function

**R(s,a,s')**

R(3,RIGHT,4) = -1 + 10

R(3,STAY,3) = -2

R(2,LEFT,3) = -1

***

### 2.Computing Returns

#### 2.1 

$$G_{0}=R_{1}+\gamma R_{2}+\gamma^{2}R_{3} \gamma^{3}R_{4} = 1+0.9*2+0.81*5=6.85$$

#### 2.2 

$$G_{0}=R_{1}+\gamma R_{2}+\gamma^{2}R_{3} \gamma^{3}R_{4} = 1+0.5*2+0.25*5=3.25$$

#### 2.3 

$$G_{n}=R_{n+1}$$

#### 2.4

>discounting determins how much the agent cares about the future rewards compared to immediate rewards
>
>The most important role is to guarantee the mathematical convergence


***

### 3.Bellman Equation Derivation
 

$$V^{\pi}(s)=E_{\pi}[G_{t}|S_{t}=s]$$

(a) show that $G_{t}=R_{t+1} +\gamma G_{t+1}$

$$G_{t}=R_{t+1}+\gamma R_{t+2}+\gamma^{2}R_{t+3}+\dots+\gamma^{n}R_{t+n+1}$$
$$G_{t+1}= R_{t+2}+\gamma R_{t+3}+\dots+\gamma^{n}R_{t+n+2}$$
$$G_{t}=R_{t+1}+\gamma G_{t+1}$$

(b) Derive the Bellman Equation

$$V^{\pi}(s)=E_{\pi}[G_{t}|S_{t}=s]$$
$$=E_{\pi}[R_{t+1}+\gamma R_{t+2}+\gamma^{2}R_{t+3}+\dots+\gamma^{n}R_{t+n+1}|S_{t}=s]$$
$$=E_{\pi}[R_{t+1}+\gamma G_{t+1}|S_{t}=s]$$
$$=E_{\pi}[R_{t+1}+\gamma V^{\pi}(S_{t+1})|S_{t}=s]$$
$$=\sum_{a\in A}\pi(a|s)\sum_{s',r}P(s',r|s,a)[r+\gamma V^{\pi}(s')]$$

(c) Explain in words what this equation means

>the second part of this equation is the definition of Q(s,a)
>
>this equation means that the state value V(s) is the weighted average of all possible Q(s,a) in the situation S

>It is recursive because the future rewards are unknown immediately


