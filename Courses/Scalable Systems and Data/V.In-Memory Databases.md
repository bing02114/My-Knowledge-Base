### 1.Database Workloads: OLAP vs. OLTP

#### 1.1 OLAP

* Deals with massive amounts of data
* Involves complex queries across many tables
* Queries are long-running but still require some level of interactivity
#### 1.2 OLTP

* Primarily consists of transactions, meaning updates
* Operations typically touch only a few tables

***
### 2.The Case for In-Memory Databases

#### 2.1 Size Reality

* Moore's Law has outpaced the growth of typical transactional database sizes
* A 1 Terabyte database is considered very large for transactional processing (TP)
* It is now financially feasible to purchase 1 Terabyte of main memory
* The implication is that if your data doesn't fit in main memory today, it likely will in a few years

#### 2.2 Performance Reality

* In traditional database management systems (DBMS), only about 4% of CPU cycles are spent on "useful work".
* The vast majority of time is consumed by overheads:

- Buffer Pool Management: 24%
    
- Locking: 24%
    
- Latching: 24%
    
- Recovery (Logging): 24%

* Simply moving to main memory gets rid of the buffer pool, which only addresses 25% of the overhead
* To achieve significant speed improvements, all major sources of overhead must be addressed

***
### 3.Morden Database Solutions

#### 3.1 OldSQL:

* Refers to traditional, legacy RDBMS vendors with code dating back to the 1980s
* They offer mediocre performance for modern transactional processing workloads.

#### 3.2 NoSQL:

* Gains performance by giving up SQL and ACID properties
* Giving up ACID means developers must handle data consistency in their application code, which is difficult.
* It is suitable for non-transactional systems or single-record, commutative transactions

#### 3.3 NewSQL:

* Aims to preserve both SQL and ACID guarantees.
* Achieves high performance and scalability through innovative, modern software architecture
* It needs to find solutions for the main overheads: locking, buffer pool, latching, and logging.

***
### 4.NewSQL Example: VoltDB

#### 4.1 Core Architecture

**Main-memory storage:** Eliminates buffer pool overhead

**Single-threaded execution:** Transactions are run to completion sequentially within each partition, which eliminates the need for locking and latching.

**Built-in replication and high availability:** This replaces traditional write-ahead logging for durability and recovery.

#### 4.2 Performance Result

With this new architecture, VoltDB spends 95% of its time on useful work, with only 5% on locking overhead.

#### 4.3 Technical Details

**Partitioning:** Data tables are either partitioned (rows spread across partitions based on a key) or replicated (a full copy exists in every partition)

**Transactions:** All database access is through Java stored procedures. A single stored procedure invocation constitutes a single ACID transaction. This limits round trips between the application and the database

**Concurrency:** The single-threaded model means other transactions must wait for the currently running transaction to complete. This makes it highly effective for OLTP but not suitable for long-running OLAP queries

**Communication:** Client applications communicate asynchronously with VoltDB for maximum throughput

***
### 5.Summary Comparison

**OldSQL for New OLTP:** Too slow and doesn't scale well.

**NoSQL for New OLTP:** Lacks consistency guarantees (ACID) and often has a low-level interface

**NewSQL for New OLTP:** It is fast, scalable, consistent, and supports SQL. 