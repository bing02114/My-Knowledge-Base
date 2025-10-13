### 1.Definition

>FLOPs stand for **Floating Point Operations**. 
>
>It is a common metric used to measure the computational complexity of a neural network model. 
>
>In essence, it quantifies the total number of floating-point arithmetic operations (like additions, subtractions, multiplications, divisions) required to perform a single forward pass through the network.

>A higher FLOPs count generally means a model is more computationally expensive, requiring more hardware resources and taking more time to execute.

**Important Note on Calculation**

>A multiply-accumulate (MAC) or multiply-add operation consists of one multiplication and one addition. In deep learning analysis, it is standard practice to count one MAC as **two** separate operations.

### 2.FLOPs Calculation for a Convolutional Neural Network

>For a standard 2D convolutional layer, the total FLOPs can be calculated based on the dimensions of the output feature map, the size of the kernel, and the number of input and output channels.

$$TotalFLOPs ≈ 2 \times H_{out} \times W_{out} \times N_{f} \times K_{h} \times K_{w} \times N_{c}$$
Where:

- Hout​, Wout​: Height and width of the output feature map. 
    
- Nf​: Number of filters (which equals the number of output channels). 
    
- Kh​,Kw​: Height and width of the convolutional kernel. 
    
- Nc​: Number of input channels.

### 3.FLOPs Calculation for an Attention-based Neural Network

#### 3.1 Dimensions

- L: Sequence length
    
- d: Feature dimension
    
- dk​: Key/Query dimension
    
- dv​: Value dimension

#### 3.2 Computational Steps

**1.Q,K,V Projection**

$$FLOPs(Q) = 2 \times L \times d \times d_k$$

$$FLOPs(K) = 2 \times L \times d \times d_k$$

$$FLOPs(V) = 2 \times L \times d \times d_v$$

**2.Score Calculation**

$$FLOPs(Score)=2 \times L \times d_k \times L=2 \times L^2 \times d_k​$$

**3.Attention Output**

$$FLOPs(Output)=2 \times L \times L \times d_v​=2 \times L^2 \times d_v​$$

**4.Final Output Projection**

$$FLOPs(Final)=2 \times L \times d_v \times d$$

