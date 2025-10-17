## 

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

``` math
G_{0}=R_{1}+\gamma R_{2}+\gamma^{2}R_{3}_\gamma^{3}R_{4}
```



