### 1.The New Bottleneck: Main Memory and Caches

#### 1.1 Hardware Trends and the "Memory Wall"

- While CPU speed and memory capacity have historically doubled every 18 months, memory performance (especially latency) grows much more slowly, at about 10% per year.
    
- This growing gap means that even for databases that can fit entirely in main memory, the time spent waiting for data from memory is a major performance limiter.

#### 1.2 The Importance of Cache Performance

- With memory access becoming the bottleneck, CPU cache performance is now crucial.
    
- The memory hierarchy (L1/L2 Cache, DRAM, etc.) means that memory access times are not uniform.
    
- Unlike the disk buffer pool, a DBMS has no direct control over the CPU cache, so algorithms and data structures must be designed to be "cache-conscious".

#### 1.3 Strategies for Improving Cache Locality

>To improve cache performance, the key is to improve data locality (both temporal and spatial).

**Techniques**

- **Clustering:** Arrange data that is accessed together to fit within a single cache line.
    
- **Packing:** Squeeze more useful data into each cache line.
    
- **Partitioning:** For random access patterns (like in a hash join), partition the data into chunks that can fit entirely within the cache to avoid thrashing.

***
### 2.Cache-Conscious Tree Indexes

#### 2.1 The B+ Tree: A Disk-Oriented Index

#### 2.2 CSS-Tree (Cache-Sensitive Search Tree): For Read-Only Workloads

#### 2.3 CSB+ Tree (Cache-Sensitive B+ Tree): Adding Update Capabilities)

#### 2.4 Performance Summary of Tree Variants

- A comparison shows a trade-off between search and insertion performance:
    
    - **Search Performance (Best to Worst):** CSS < CSB+ < B+
        
    - **Insertion Performance (Best to Worst):** B+ < CSB+ < CSS
        
- **Conclusion:** The CSS-Tree is best for read-only environments, while variants like the Full CSB+ tree offer a good balance if space is not a concern and updates are frequent.

***
### 3.Cache-Conscious Join Algorithms

#### 3.1 Prerequisite: Vertical Decomposed Storage

- A storage model where a table is divided into separate arrays for each attribute (column).
    
- This improves cache locality for queries that only access a subset of columns, as irrelevant data is not loaded into the cache.

#### 3.2 Problems with Traditional Join Methods

- **Sort-merge and Hash Joins** perform poorly if one of the relations does not fit into the CPU cache.
    
- This leads to **cache thrashing**, where data is constantly being evicted from and reloaded into the cache, resulting in a cache miss for nearly every tuple access.

#### 3.3 Radix Join: A Cache-Friendly Approach

- A multi-pass join algorithm designed to avoid cache thrashing.
    
- **Partitioning Phase:** It recursively partitions both tables based on the bits of the join attribute. The number of partitions in each pass is deliberately kept small enough to ensure that the data needed for the partitioning step fits within the cache.
    
- **Join Phase:** Once the partitions are small enough to fit in the cache (e.g., L1 size), a simple hash join or nested-loop join is performed on each pair of matching partitions.

### 4.Summary and Key Lessons

- **Core Principles of Cache-Conscious Design:**
    
    - Cache performance is critically important for modern in-memory systems.
        
    - The main goal is to **improve locality** by:
        
        1. Clustering related data into cache lines.
            
        2. Leaving out irrelevant data (e.g., pointer elimination, vertical decomposition).
            
        3. Partitioning large data structures to avoid cache and TLB thrashing.
            
- **Application to Spatial Data:**
    
    - For in-memory spatial indexes like R-Trees, the bottleneck shifts from I/O to computation.
        
    - Cache-conscious principles still apply, such as storing objects that are physically near each other in the same cache line to improve query performance.