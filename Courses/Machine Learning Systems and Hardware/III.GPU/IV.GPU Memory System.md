### 1.Memory Hierarchy

>GPUs have a complex memory hierarchy with different speeds, sizes, and scopes:

* **Registers**: Faster memory, private to each thread
* **L1 Cache / Shared Memory**: On-chip memory, much faster than global memory. Shared memory is shared among threads within the same thread block
* **L2 Cache**: A larger cache shared by all SMs to buffer global memory accesses
* **Global Memory (DRAM)**: The largest but slowest memory, accessible by all threads on the GPU

### 2.Memory Coalescing

>To achieve high memory bandwidth, it's critical that threads in a warp access contiguous locations in global memory. When memory access is scattered, the hardware must issue multiple memory transactions, wasting bandwidth. This is a key optimization target in CUDA programming