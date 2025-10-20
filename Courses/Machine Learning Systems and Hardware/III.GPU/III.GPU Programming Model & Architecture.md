### 1.Programming Model

#### 1.1 Host and Device

>CUDA programming involves `Host` code that runs on the CPU and `Device` code (called a kernel) that runs on the GPU. A typical workflow involves the CPU copying data to the GPU, launching the kernel on the GPU for parallel computation, and then copying the results back

#### 1.2 SIMT

>The core programming model for GPUs. It extends the SIMD concept by issuing one instruction to multiple independent threads

#### 1.3 Hierarchical Structure

**Thread**

>The basic unit of execution

**Thread Block**

>A group of threads that can cooperate by sharing memory and synchronizing their execution

**Grid**

>A collection of thread blocks that execute the same kernel

***
### 2.Hardware Architecture
#### 2.1 Streaming Architecture

>The core execution unit of an NVIDIA GPU. A modern GPU contains many SMs. Each SM consists of

* **CUDA Cores**: ALUs that perform integer and floating-point arithmetic
* **Special Function Units**: Hardware for accelerating complex math functions like sine, cosine, and square root
* **Tensor Cores**: Specialized hardware units introduced since the Volta architecture to accelerate the matrix multiplication operations that are central to AI workloads

#### 2.2 Warp

>Threads are executed in groups of 32 (on NVIDIA GPUs), known as a warp. All threads in a warp execute the same instruction at the same time.

#### 2.3 Warp Divergence

>A significant performance issue that occurs when threads within the same warp take different paths in a conditional branch (e.g., `if-else`). This forces the paths to be executed serially, leading to idle cycles and under-utilization