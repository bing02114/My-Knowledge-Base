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

