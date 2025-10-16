### 1.Continuous Value Handling

#### 1.1 Strategy

>Use a binarization (bi-partition) technique. This is the mechanism used in the C4.5 algorithm

#### 1.2 Process

>Given a dataset D and a continuous attribute _a_, sort the _n_ distinct values of _a_ as {a1,a2,...,an}. The set of candidate split points is:

$$T_{a}=\{\frac{a^{i}+a^{i+1}}{2}|1\leq i\leq n-1\}$$

**Choose the split point that maximizes the information gain.** 

**Note**: Unlike discrete attributes, a continuous attribute can be used as a splitting attribute **for its descendant nodes.**

### 2.Missing Value Handling

>This addresses two problems: 
>
>(1) how to select a splitting attribute when some values are missing, and 
>
>(2) how to partition samples when a sample is missing a value for the chosen attribute. The C4.5 algorithm provides a solution.


#### 2.1 how to select a splitting attribute when some values are missing

>Calculate information gain using only the subset of samples D~ that have no missing values for attribute _a_. The gain is weighted by the ratio ρ of samples without missing values for that attribute

$$Gain(D,a)=\rho\times Gain(\widetilde{D},a)$$

#### 2.2 how to partition samples when a sample is missing a value for the chosen attribute

>If a sample _x_ has a missing value for attribute _a_, it is partitioned into all sub-nodes corresponding to the possible values of _a_. The weight of sample _x_ is adjusted in each sub-node to be $\widetilde{r}_{v}·w_{x}$, where r~v​ is the proportion of non-missing samples with value $a^{v}$

