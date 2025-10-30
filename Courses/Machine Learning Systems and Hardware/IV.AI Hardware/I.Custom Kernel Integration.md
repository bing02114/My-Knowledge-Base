### 1.Why Custom Kernels

* **Optimizing for new architecture**: To get the best performance from new hardware like the Blackwell architecture
* **Developing new algorithms**: Standard libraries like PyTorch/Tensorflow may not have built-in operations for all new algorithmic needs
* **Improving hardware performance**:  By using custom computation patterns, fusions, and other optimizations. An example is FlashAttention, which uses I/O and memory optimizations

### 2.FlashAttention-1: Key Idea

* **Operator Fusion**: Combining multiple operations into a single kernel to reduce memory traffic. The time taken by a standard PyTorch implementation of attention is broken down into Matmul, Dropout, Softmax, and Mask operations, whereas FlashAttention combines these into a single "Fused Kernel"
* **Block tiling**: Separating the large Q, K, V matrices into smaller blocks (tiles) and caching them in the fast on-chip SRAM. This also involves decomposing the large softmax operation
* **Re-computation**: Instead of storing large intermediate matrices (like the attention matrix S), they are recomputed from the blocks of Q, K, V in SRAM during the backward pass.

### 3.Integration Paths

**CUDA Kernel + Python Binding**:

* **Pros**: Provides fine-grained, low-level control and can achieve high performance when fully optimized

* **Cons**: Has a longer development and debugging cycle

**Triton Kernel Programming**

* **Pros**: Offers high productivity through a mid-level abstraction, using Python code that is easy to integrate with PyTorch.

* **Cons**: It is less flexible for low-level tuning and may result in lower performance compared to CUDA


### 4.Triton: A Domain-Specific Language (DSL)

* It is an open-source, Python-based DSL for writing GPU kernels.
* It abstracts away low-level details such as memory coalescing, shared memory management/synchronization, and tensor core scheduling. For example, Triton handles memory coalescing, shared memory, and within-SM scheduling automatically, whereas CUDA requires manual management
* The programming model is SIMD-like, focusing on blocks of elements (tiles) rather than individual threads.
* Triton provides an `@triton.autotune` decorator to automatically test different configurations (e.g., `BLOCK_SIZE`) and find the best one for a given problem size.

