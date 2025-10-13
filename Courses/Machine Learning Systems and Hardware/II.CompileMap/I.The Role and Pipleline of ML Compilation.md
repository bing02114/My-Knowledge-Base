### 1.Why Compilation is Necessary

#### 1.1 Algorithmic Complexity ≠ Hardware Performance

>Depth-wise convolution: fewer FLOPs but limited parallelism, high
>memory bandwidth cost

End-to-End performance depends on:

$$e2e\_Perf = F(FLOPs,Infrastructure,Hardware)$$
#### 1.2 Role of ML compilers

* Bridge between algorithm and hardware
* Decide how computation is scheduled, fused and mapped to specific hardware units
* Translate algorithmic improvements into real speed-up

### 2.The Five Stages of an ML Compiler

#### 2.1 Front-end API for model construction

**Imperative Programming**

>**Philosophy**: Build and Execute (Pytorch)
>
>**Advantages**:
>
>* Easier for debugging: inspect tensors at any point
>
>* Beginner-friendly: familiar Python control flow

**Declarative Programming**

>**Philosophy**: Build then Execute (Early version of TensorFlow)
>
>**Advantages**:
>
>* Easier for compilers to optimize
>
>* Well-suited for distributed execution and batching

#### 2.2 Dataflow graph construction

Why

Representation (DAG):

Inference

Training

#### 2.3 Intermediate Representation

#### 2.4 Graph/Tensor Optimations
