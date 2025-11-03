### 1.Introduction: Why Efficient ML

#### 1.1 Goal

>End-to-end performance (e2e_Perf) is a function of the Algorithm (FLOPs), Infrastructure, and Hardware

#### 1.2 Performance Gains

>Single-chip inference performance has improved 1000x in 10 years (up to 2023)

#### 1.3 Source of Gains

>The largest gains come from efficient ML algorithms

***
### 2.The Four Levels of Efficient ML Opportunties

1. **Precision/Bit-level (精度/比特层):** Quantization (量化
2. **Scalar/Tensor-level (标量/张量层):** Pruning / Sparsification (剪枝/稀疏化)
3. **Operator-level (算子层):** Efficient ML Operations (高效机器学习算子)
4. **Architecture-level (架构层):** Neural Architecture Search (神经架构搜索)

***
### 3.Level1 : Quantization

#### 3.1 Definition

>Representing weights and/or activations with lower-precision data types (e.g., FP32 → INT8, INT4). This can include extreme cases like binary (1-bit) networks.

#### 3.2 Benefits

* **Reduced Memory (减少内存):** Lowers memory footprint and bandwidth. For example, Llama-7B drops from ~28 GB (FP32) to ~7 GB (INT8).
* **Energy Efficiency (提升能效):** Simpler arithmetic and lower bitwidth lead to better energy efficiency
* **Higher Compute Density (更高计算密度):** Low-bit units deliver better FLOPs/mm2.

#### 3.3 Key Data Types

**Floating Point(FP)**

>Composed of Sign, Exponent (for dynamic range), and Mantissa (for precision). FP8 (E4M3/E5M2) is emerging for AI.

**Fixed Point(FixP)**

>Composed of Sign, Integer, and Fraction bits.

**Emerging Data Types**

* **Block Floating Point (BFP) (块浮点):** Shares a single exponent across a block of numbers to save memory
* **Microscaling (MX) (微缩放):** An industry-standard format that uses a shared scale (X) for a block of _k_ scalar elements. Examples include MXFP8, MXFP4, and MXINT8

#### 3.4 Quantization Paradigms

**Post-Training Quantization (PTQ)**

* **Workflow (工作流):** A pre-trained model (e.g., in FP32) is calibrated using a small dataset, and then quantized.
* **Pros (优点):** Fast deployment, no retraining required
* **Cons (缺点):** May incur significant accuracy loss

**Quantization-Aware Training (QAT)**

* **Workflow (工作流):** Incorporates quantization error during the finetuning or retraining process. It often uses **"Fake Quantization"** to simulate the low-precision effects (Quantize → De-Quantize) while computation remains in high-precision
* **Pros (优点):** Helps maintain accuracy, even at very low bit-widths (e.g., FP4)
* **Cons (缺点):** Time-consuming training process.

#### 3.5 Quantization Schemes

**Linear Quantization**

>Uses an affine mapping r=S(q−Z), where S is the "scale factor" and Z is the "zero point".

**Symmetric vs. Asymmetric**

* **Symmetric (对称):** Zero-centered (Z=0), simpler for hardware.
* **Asymmetric (非对称):** Not zero-centered (Z=0), allows for better use of the quantization range, especially for non-centered data.

**Granularity**

>Refers to the block size for sharing scale/zero-point.

* **Per-Layer (层级):** One scale/ZP for the entire layer. Low metadata cost, but can have large errors.
* **Per-Channel (通道级):** One scale/ZP per filter. Lowest error, but high metadata cost.
* **Per-Group (分组级):** A balance between the two.

**Static vs. Dynamic**

* **Static (静态):** Quantization parameters are fixed ahead of time (offline).
* **Dynamic (动态):** Parameters are adjusted during runtime based on data distribution.

***
### 4.Level2 : Pruning / Sparsification

#### 4.1 Definition

>Reducing model size by removing redundant or unnecessary weights

#### 4.2 Process

1. **Train Connectivity (训练连接):** Train the network normally
2. **Prune Connections (剪除连接):** Remove low-weight connections.
3. **Train Weights (训练权重):** Retrain the network with the sparse connections.

#### 4.3 Pruning Granularity

* **Point-wise (or Unstructured) (逐点/非结构化):** Removes individual elements. Achieves high sparsity but is hard for hardware to accelerate.
* **Channel-wise (or Structured) (逐通道/结构化):** Removes entire channels or filters. This maps cleanly to regular hardware operations.
* **Layer-wise (逐层):** Removes an entire layer.
* **Expert-wise (逐专家):** Specific to Mixture-of-Experts (MoE) models, pruning low-utility experts

#### 4.4 Hardware Support

>Modern accelerators like NVIDIA Ampere GPUs offer native support for N:M structured sparsity (e.g., 2:4 sparsity, meaning 2 non-zero weights out of every 4). (现代加速器（如 NVIDIA Ampere GPU

***
### 5.Level3 : Efficient ML Operators

#### 5.1 Definition

>Using operators where efficiency and sparsity are inherent to their design, rather than applied afterward.

#### 5.2 Examples

* **Multi-Head Attention (MHA) (多头注意力):** The standard, with separate Query (Q), Key (K), and Value (V) projections for each head.
* **Multi-Query Attention (MQA) (多查询注意力):** All query heads share a single Key and Value. This dramatically reduces memory and computation.
* **Grouped-Query Attention (GQA) (分组查询注意力):** A balance where K and V are shared _within groups_ of query heads. This is used in LLaMA-2.
* **Multi-Head Latent Attention (MLA) (多头潜在注意力):** Reduces the KV cache size by using latent space projection (compression)
* **Depth-wise Convolution (深度可分离卷积):** An efficient convolution variant.

***
### 6.Level4 : Neural Architecture Search

#### 6.1 Definition

>The process of automatically designing optimal neural network architectures.

#### 6.2 NAS Methods

**Reinforcement Learning (RL)-based**

* **Process (流程):** Uses an RNN (the "controller") to sample an architecture (the "child network"). The child network is trained to get an accuracy (the "reward") , which is then used to update the controller via policy gradient.
* **Drawback (缺点):** Extremely high computational cost (e.g., 800 GPUs for 28 days)

**Gradient-based**

* **Key Idea (核心思想):** Differentiable Architecture Search (DARTS). It uses **"continuous relaxation"** by parameterizing the choice of an operation as a softmax over all possible operations.
* **Process (流程):** This makes the architecture itself differentiable, allowing the architecture parameters (α) and weights (w) to be optimized jointly with gradient descent.
* **Drawback (缺点):** High memory consumption and no hardware-awareness.

**ProxylessNAS**

* **Key Idea (核心思想):** Addresses the issues of DARTS by constructing an over-parameterized "super-net" with binary gates.
* **Process (流程):** It samples only one path at a time to reduce memory cost and introduces **expected latency** into the loss function, making the search hardware-aware.



