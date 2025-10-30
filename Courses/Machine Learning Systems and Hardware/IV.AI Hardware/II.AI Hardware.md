### 1.Domain-Specific Architecture (DSA)

* While GPUs dominate AI due to their mature software ecosystem (CUDA) and massive parallelism, they are not always energy-efficient because they are designed for many domains, not just AI
* DSAs trade generality for efficiency by tailoring the architecture for specific workloads like AI.
* Examples include Google's TPU, Samsung's NPU, and Tesla's Dojo.

### 2.Systolic Array

* **Concept**: Proposed by Kung & Leiserson in 1979, it is an array of chained processing elements (PEs) where data flows step-by-step like a "wave," enabling multiple computations for each memory access. This structure is the basis of the Google TPU's Matrix Multiply Unit.
* **Motivation**: A naïve design for matrix multiplication where each input buffer broadcasts data to all PEs suffers from high fan-out, leading to excessive wiring, delays, and power consumption. The systolic array solves this by chaining PEs locally, reducing fan-out and improving scalability.
* **Streamflow Strategies**: Different strategies exist for moving data through the array for matrix multiplication, each with pros and cons
	* **Output-Stationary**：The output matrix C remains stationary in the PEs, while input matrices A and B are streamed through. This is good for large reduction dimensions but has low data locality for weights
	* **Weight-Stationary**: Weights (e.g., matrix A or B) are kept stationary in the PEs, while activations and partial sums stream through. This allows for good data reuse for weights.

### 3.Scale-Up vs. Scale-Out

* **Scale-Up**: Adding more compute resources _within one node_ (e.g., a single server with multiple GPUs connected by NVLink/NVSwitch).
* **Scale-Out**: Adding more nodes to a cluster, with each node having its own memory and accelerators, connected by networking like InfiniBand or optical switches

### 4.Reconfigurable Architecture

* **Concept**: Hardware that can adapt its structure for different tasks, offering a trade-off between the high performance/efficiency of fixed hardware (ASICs) and the high flexibility of general-purpose hardware (CPUs)
* **FPGA (Field-Programmable Gate Array)**: A fine-grained reconfigurable architecture based on Configurable Logic Blocks (CLBs), memory, and programmable interconnects. They offer bit-level control and are well-suited for low-latency and edge AI workloads. Major vendors include Xilinx (AMD) and Altera (Intel)
* **CGRA **(Coarse-Grained Reconfigurable Array)****: A block-level reconfigurable architecture that sits between FPGAs and GPUs in terms of flexibility and efficiency. It uses coarse-grained PEs like ALUs, offering better performance than FPGAs but less flexibility. An example is the SambaNova Reconfigurable Dataflow Unit (RDU).