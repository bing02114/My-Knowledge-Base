### 1.The Performance Problem: Databases and Modern CPUs

#### 1.1 The Memory Wall

* Traditional database systems are often memory-bound, not CPU-bound
* Processors spend a significant amount of time stalled, waiting for data from memory. For some database workloads, this can be more than 50% of the execution time.
* Modern OLTP (Online Transaction Processing) benchmarks like TPC-C and TPC-E running on multicore systems show low Instructions Per Cycle (IPC), often less than 1.
* This low IPC is due to high stall rates, with CPUs being stalled for up to 70% of the execution time. The majority of these stalls are memory-related

***
### 2.The Evolution of Hardware: The Multicore Era

#### 2.1 Moore's Law and Its Shift

* While the number of transistors on a chip continues to double (Moore's Law), single-core clock speeds and power consumption have hit a wall.
* The industry's response has been to move towards multi-socket and multicore architectures to continue scaling performance.

#### 2.2 Modern CPU Architecuture

* **Vertical Dimension:** Consists of multiple cores, each with its own L1 and L2 caches, sharing a larger L3 cache (Last-Level Cache, LLC) before accessing main memory.
* **Horizontal Dimension:** Consists of multiple sockets (processors), each containing multiple cores. These sockets are connected via inter-socket links
* **NUMA (Non-Uniform Memory Access):** This multi-socket architecture creates "hardware islands". Accessing memory connected to the local socket is fast, while accessing memory on a remote socket is significantly slower

***
### 3.Strategies for Minimizing Memory Stalls

#### 3.1 Prefetching

* Techniques like next-line, stream, and stride prefetching are used by hardware to fetch data before it's explicitly requested, favoring sequential access patterns
* More advanced software-guided prefetching can explicitly fetch required instructions or data, such as B-tree nodes, ahead of time.

#### 3.2 Cache-Conscious Data Layouts and Structures

* **Row vs. Column Stores:** Row stores are better for OLTP workloads that access many columns of a single record, while column stores are better for OLAP workloads that access few columns of many records. This is because column stores maximize the use of each cache line by packing relevant data together
* **Data Structures:** Index trees like B-trees should have their nodes aligned to cache lines to maximize cache line utilization during a tree traversal.

#### 3.3 Cache-Conscious Execution Models

* **Vectorized Execution:** Processes data in batches (vectors) rather than one tuple at a time (Volcano Iterator Model). This improves both data and instruction cache locality

***
### 4.Scaling OLTP on Multicores: The Contention Problem

#### 4.1 The Scalability Bottleneck

* Unlike OLAP which is memory-bandwidth limited, OLTP throughput often peaks and then drops as the number of threads increases. This is due to contention on shared data structures
* Even the simplest transaction involves many critical sections for locking, latching, logging, and buffer pool management.

#### 4.2 Unscalable Components

* The primary bottlenecks to scalability in traditional OLTP systems are **locking, latching, and logging**

***
### 5.Solutions for Scalable OLTP

#### 5.1 Addressing Locking Contention

* **Speculative Lock Inheritance (SLI):** To reduce contention on hot locks, a transaction commits without releasing its hot locks and instead passes them directly to the next transaction that is likely to need them. This significantly reduces lock manager contention.

#### 5.2 Adressing Latching Contention

* **Physiological Partitioning (PLP):** Instead of having a single centralized data structure (like a B-tree) protected by latches, the data is logically partitioned. Each partition is managed by a specific worker thread, effectively creating private, latch-free data structures (like a multi-rooted B-tree) and converting unpredictable global data accesses into predictable local ones

#### 5.3 Addressing Logging Bottlenecks

* **Aether (Holistic Logging):** Traditional write-ahead logging (WAL) creates a serial bottleneck. Aether improves this with techniques like flush pipelining, where multiple transactions' log records are batched together by a dedicated log writer thread, reducing context switches and contention