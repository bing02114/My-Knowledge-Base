### 1.Workflow Scheduling with DAGs

>This document focuses on workflow scheduling, where job dependencies are represented by **Directed Acyclic Graphs (DAGs)**. In a DAG, the vertices are jobs, and a directed edge from job 'i' to job 'j' signifies a precedence constraint: job 'i' must be completed before job 'j' can begin. These precedence constraints often result in "forced idleness," where a machine may be free but cannot start a job because its prerequisite jobs are not yet finished.

Scheduling problems with general precedence constraints are very difficult; most are NP-hard, and for many, the complexity is still an open question. Optimal solutions are typically known only under restrictive assumptions, such as:

* All jobs have unit processing times (pj​=1).
* There is a fixed, small number of machines (e.g., two).
* The DAG has a restricted topology, like chains, in-trees (each node has at most one child), or out-trees (each node has at most one parent).

### 2.Hu's Critical Path Algorithm

>Hu's algorithm is a famous optimal method for solving the problem of minimizing makespan on parallel machines where jobs have unit processing times and form an in-tree precedence structure (P∣i.t.,pj​=1∣Cmax​).

>The algorithm works as a list scheduler by first assigning a level (αj​) to each job. The level is determined by the length of the longest path from that job to the final "exit node" of the in-tree. Jobs with a higher level (i.e., on a longer path to completion) are given higher priority. The longest path in the graph is called the **critical path**.

>hu's algorithm is also optimal for out-trees (P∣o.t.,pj​=1∣Cmax​) and for scheduling a set of disjoint in-trees. For general precedence graphs with unit processing times (P∣prec,pj​=1∣Cmax​), it serves as an approximation algorithm.


### 3.Muntz-Coffman Algorithm

>This algorithm is an extension of Hu's algorithm that applies to the _preemptive_ scheduling case, where jobs can be interrupted and resumed. It is notably optimal for several problems, including general DAGs on two machines with unit processing times (P2​∣pmtn,prec,pj​=1∣Cmax​)

>The core idea is to partition jobs into a **subset sequence** (S1​,S2​,...,Sk​). This sequence ensures that if a job in subset Sj​ depends on a job in subset Si​, then it must be that j>i. The algorithm generates this sequence by prioritizing jobs with higher levels (critical path first) while also trying to keep the machines busy.

>Once the subset sequence is created, the schedule is constructed. If a subset Sj​ has more jobs than available machines, McNaughton's wrap-around rule is used to schedule them preemptively. For the general preemptive problem (P∣pmtn,prec∣Cmax​), the Muntz-Coffman algorithm provides a good approximation with a worst-case ratio of R=2−2/m.








