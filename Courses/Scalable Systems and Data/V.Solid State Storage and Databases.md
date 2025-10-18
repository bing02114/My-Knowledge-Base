### 1.Flash Disks Fundamentals

#### 1.1 Role in System

* Can be used as a secondary storage or a caching layer

#### 1.2 Key Characteristics

* **Advantage:** Random reads are equally as fast as sequential reads
* **Disadvantage:** Random writes are slow.

#### 1.3 Internal Organization

* Data is organized into pages, which are then organized into flash blocks
* An SSD consists of interconnected flash chips, an internal CPU, internal memory, and a flash controller.
* It has no mechanical limitations and maintains a block API to be compatible with traditional disk layouts

#### 1.4 Flash Translation Layer (FTL)

* The FTL is a complex device driver (firmware) that tunes performance and the device's lifetime

***
### 2.Comparison: Flash Disks vs. HDD

#### 2.1 HDD (Hard Disk Drive)

* Offers large, inexpensive capacity
* Suffers from inefficient random reads

#### 2.2 Flash Disks (SSD)

* Capacity is smaller and more expensive
* Provides very efficient random reads

#### 2.3 Role in the Stroage Hierachy

* In the past, there was a latency gap of 2-3 orders of magnitude between RAM and HDD
* Today, Solid State Memory (SSM), like Flash, helps to bridge the significant latency and bandwidth gap between RAM and HDD.

***
### 3.Flash/SSD Impact on Databases

#### 3.1 Traditional DBMS Design

* Database Management Systems (DBMS) have traditionally been designed from the ground up based on an HDD model.
* Common optimizations for HDDs include B-trees, preferring sequential access, buffer pools, and write-ahead logging

#### 3.2 Positioning Flash in the System

* Flash can be used in several ways: as a complete HDD replacement, as an intermediate layer between RAM and HDD, or side-by-side with HDDs.
* The correct use depends on the specific workload, such as dataset size and access patterns.

***
### 4.Database Use Cases with Flash/SSD

#### 4.1 Use Case 1:Flash-only OLTP

* OLTP workloads are dominated by random reads and writes, which are much faster on flash.
* **Challenge:** The slow random write speed of flash can cause throughput to degrade significantly over time
* **Solution:** Use an "Append/Pack" method which avoids in-place updates by writing sequentially, thus mitigating the random write problem

#### 4.2 Use Case 2:Flash-aided Business Intelligence

* **Challenge:** Data warehouse workloads involve both read-only queries (scans) and scattered updates, and combining them efficiently is difficult.
* **Solution:** Use flash as a large-capacity write cache for incoming updates. Queries then merge data from the main dataset on HDDs with the recent updates stored on the flash cache
* The **Materialized Sort-Merge (MaSM)** method demonstrates this approach, showing negligible impact on large scans and only a small overhead for point queries

#### 4.3 Use Case 3:Logging on Flash+HDD

* **Challenge:** Transactional logging is a major bottleneck for modern OLTP databases that can fit into main memory, as they still must flush logs to stable media.
* The access pattern for logs consists of small, sequential writes, which causes full rotational delays on HDDs.
* **Solution:** Flash is well-suited for this pattern. The log can be written to an in-memory buffer and then flushed to multiple flash devices by worker threads

***
### 5.Conclusion

* Solid State Memory (SSM) can effectively help bridge the I/O gap between RAM and HDD
* However, software, particularly the DBMS, needs to be adapted or redesigned to fully leverage the benefits of this new hardware layer.
* The field of SSM is rapidly evolving, with many potential uses in data management and several promising commercially viable technologies on the horizon