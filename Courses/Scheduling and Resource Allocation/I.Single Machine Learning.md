### 1.Basic Assumptions

* A1: A set of n jobs is ready to be scheduled immediately
* A2: Processing times are deterministic and known in advance
* A3: No preemption is allowed, meaning a job cannot be interrupted once it has started
* A4: There is only a single server machine available
* A5: There are no explicit setup times between jobs
* A6: The machine does not idle if there are job waiting

### 2.Scheduling Policies and Optimality

#### 2.1 Minimizing Makespan (1||Cmax)

>This objective aims to minimize the completion time of the very last job. The document states this problem is trivial because the makespan is simply the sum of all processing times (Cmax​=∑pj​), which is a constant regardless of the job sequence. Therefore, any random schedule is optima

#### 2.2 Minimizing Total Completion Time (1||∑Cj)

>To minimize the sum of the completion times of all jobs, the optimal policy is the **Shortest Processing Time (SPT)** rule. This means scheduling jobs in non-decreasing order of their processing times. The rationale is that placing shorter jobs first gives them smaller completion times, and this has a cascading effect that reduces the overall sum, as shorter jobs contribute more times to the total sum (∑Cj​=np[1]​+(n−1)p[2]​+...+p[n]​).

#### 2.3 Minimizing Total Weighted Completion Time (1||∑wjCj)

>When jobs have different weights (priorities), the goal is to minimize the weighted sum of completion times. The optimal policy is the **Weighted Shortest Processing Time (WSPT)** rule, also known as Smith's rule. This rule schedules jobs in non-decreasing order of their processing time to weight ratio (pj​/wj​). The proof of its optimality is demonstrated using an "adjacent pairwise interchange argument" , which shows that if any two adjacent jobs are not in WSPT order, swapping them will improve the total weighted completion time.

### 3.Extension to Job Chains

>The document extends the WSPT rule to scenarios with precedence constraints, where jobs form chains

#### 3.1 Case 1: Non-interruptible Chains

>If entire chains must be processed without interruption from other chains, the scheduling rule is to treat each chain as a single "job". The chains should be scheduled in non-decreasing order of their aggregate ratio: ∑wj​∑pj​​.

aggregate ratio:

$$\frac{\sum p_j}{\sum w_j}$$

#### 3.2 Interruptible Chains

>If jobs from different chains can be interleaved, the **Chain Method** is optimal. This method involves

1. For each chain, calculate its **p-factor**, which is the minimum p/w ratio found among all its initial sub-chains

$$\rho_{A}=\min_{1\leq l\leq k}\frac{\sum^{l}_{j=1}p_j}{\sum^{l}_{j=1}w_j}$$

2. Select the chain with the smallest p-factor.
3. Schedule the initial sub-chain that determines this smallest p-factor.
4. Remove the scheduled jobs and repeat the process until all jobs are scheduled.

### 4.Schedluing with Uncertain Processing Times

>The document also considers a more realistic scenario where processing times are uncertain and are treated as random variables. This relaxes the "deterministic times" assumption (A2). In this stochastic setting, the objective is to optimize the _expected_ value of the performance measure.

The optimal policies are direct extensions of their deterministic counterparts:

* **Shortest Expected Processing Time (SEPT)**: To minimize E[∑Cj​], schedule jobs in non-decreasing order of their _mean_ processing time, E[pj​]
* **Weighted Shortest Expected Processing Time (WSEPT)**: To minimize E[∑wj​Cj​], schedule jobs in non-decreasing order of the ratio E[pj​]/wj​. This is also known as the **cμ rule** when times are exponentially distributed
