### 1.Job Release Times

>This document discusses single machine scheduling problems where jobs have specific **release times (rj​)**. A job 'j' cannot be scheduled before its release time, t≥rj​. This introduces the possibility of **forced idleness**, where the machine might have to wait for the next job to become available, even if the machine is free


### 2.Complexity of Non-Preemptive Scheduling with Release Times

>The introduction of release times significantly changes the complexity of scheduling problems.

#### 2.1 Minimizing Makespan (1|rj|Cmax)

>This problem remains simple (trivial). The optimal strategy is to keep the machine busy whenever there is a ready job. Policies like First-In-First-Out (FIFO) or scheduling ready jobs in a random order can achieve the minimum makespan.

#### 2.2 Mimizing Total Completion Time (1|rj|∑Cj)

>Unlike the case without release times, this problem becomes **NP-hard**. Simple extensions of the Shortest Processing Time (SPT) rule are no longer optimal. The document demonstrates this by showing that

* **SPT-A** (waiting for the next overall shortest job) is not optimal.
* **SPT-B** (choosing the shortest job among those currently ready) is not optimal.
* **SPT-B** (choosing the shortest job among those currently ready) is not optimal.

### 3.Preemptive Scheduling with Release Times

>When preemption is allowed, the problem of minimizing total completion time (1∣rj​,pmtn∣∑Cj​) becomes solvable in polynomial time

#### 3.1 SRPT

>The optimal policy is the **Shortest Remaining Processing Time (SRPT)** rule.

* This rule states that at any point in time t, the machine should preemptively work on the available job with the least amount of processing time remaining, xj​(t).
* The optimality of SRPT can be proven with an interchange argument, similar to the one used for SPT
* However, this optimality does not extend to the weighted case (1∣rj​,pmtn∣∑wj​Cj​), which remains NP-hard.

### 4.An Approximation Algorithm for the NP-hard Problem

>Since the non-preemptive problem 1∣rj​∣∑Cj​ is NP-hard, the document presents an approximation algorithm called the **Convert-Preemptive Schedule** method

This method is a **2-approximation**, meaning its solution is guaranteed to be no worse than twice the optimal solution. The steps are

* First, solve the preemptive version of the problem (1∣rj​,pmtn∣∑Cj​) using the optimal SRPT rule
* Then, schedule the jobs non-preemptively in the same order as their completion times in the SRPT schedule. If the next job in the sequence is not yet released, the machine waits for it.

>The proof for the approximation ratio relies on the fact that the completion time of any job in the converted schedule, Cj​(SC​), is less than or equal to twice its completion time in the SRPT schedule, Cj​(SSRPT​). Since the optimal SRPT schedule is always better than or equal to the optimal non-preemptive schedule, the 2-approximation is established.