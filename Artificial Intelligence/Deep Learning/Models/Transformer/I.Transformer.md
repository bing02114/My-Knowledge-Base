### 1.Core Idea: Why Abandon RNN/LSTM

#### 1.1 Limitations of RNN/LSTM

**Sequential Computation**

>RNNs and their variants (like LSTM, GRU) process data sequentially, step by step. This means the computation at time step t must wait for the computation at step t−1 to finish. This dependency makes them difficult to parallelize, limiting training speed on modern large-scale hardware (like GPUs/TPUs).

**Long-Range Dependency Problem**

>Although LSTMs and GRUs alleviate the vanishing/exploding gradient problem with gating mechanisms, capturing relationships between distant words in very long sequences remains challenging. Information has to travel through many steps to get from one end of the sequence to the other, leading to potential information loss.

#### 1.2 The Transfomer's Solution

**Full Parallelization**

>The attention mechanism allows the Transformer to directly calculate the relationship between any two positions in a sequence without sequential propagation. This enables the model's computations to be highly parallelized, dramatically improving training efficiency.

**Directly Capturing Long-Range Dependencies**

>For any two words in a sequence, the attention mechanism can establish a direct connection with a path length of O(1). This makes it much easier for the model to capture long-range dependencies.

***
### 2.Overall Architecture of the Transformer


![](Models/Transformer/images/transformer.png)

#### 2.1 Encoder

>It is a stack of N identical layers (N=6 in the original paper). Each layer has two main sub-layers: a **Multi-Head Self-Attention Mechanism** and a **Position-wise Feed-Forward Network**.

#### 2.2 Decoder

>The right part of the diagram. It is also a stack of N identical layers. Each layer has three main sub-layers: a **Masked Multi-Head Self-Attention Mechanism**, an **Encoder-Decoder Attention Mechanism**, and a **Position-wise Feed-Forward Network**.

#### 2.3 Residual Connections and Layer Normalization

>A residual connection is applied around each of the sub-layers, followed by layer normalization. The output of each sub-layer is `LayerNorm(x + Sublayer(x))`. This helps prevent vanishing gradients and stabilizes the training process.

***
### 3.Detailed Breakdown of Core Components

#### 3.1 Input Processing

**Word Embedding**

>Like all NLP models, the input text sequence (words or sub-words) is first converted into fixed-dimensional vectors via an embedding layer.

**Positional Encoding**

>**Problem**
>
>The self-attention mechanism itself contains no information about the order of the sequence. If you swap two words in a sentence, the attention scores might be identical, which is incorrect.
>
>**Solution**
>
>Add "positional encoding" vectors to the word embedding vectors. These vectors provide information about the absolute or relative position of a word in the sequence
>
>**Implementation**
>
>The paper uses sine and cosine functions of different frequencies to generate these en
>codings: 
> 
> $$PE_{(pos,2i+1)}=\cos(pos / 10000^{2i/d_{\text{model}}})$$
> 
> Where $pos$ is the position of the word, $i$ is the dimension index, and $d_{\text{model}}$ is the embedding dimension. This design allows the model to learn relative positional information, because for any fixed offset $k$, $PE_{pos+k}$ can be represented as a linear function of $PE_{pos}$. 

#### 3.2 Self-Attention Mechanism

>For each word vector in the input sequence, we create three vectors by multiplying it with three different weight matrices (WQ,WK,WV): a **Query** vector, a **Key** vector, and a **Value** vector.

* **Query (Q)**: Represents the current word being processed; it's looking for information
* **Key (K)**: Represents all the words in the sequence that can be queried; it acts like a "label" to be matched with the Query
* **Value (V)**: Represents the actual content of a word. Once a Query matches with a Key, its corresponding Value is what's taken

**Calculation Process**

1. **Calculate Score:** For a given Query, calculate its dot product with all the Keys. This score determines how much attention to place on other words when processing the current word.
2. **Scaling:** Divide the scores by a scaling factor (where dk​ is the dimension of the Key vector). This prevents the dot products from becoming too large, which could lead to very small gradients.
3. **Softmax:** Pass the scaled scores through a Softmax function to get a weight distribution, where all weights sum to 1.
4. **Weighted Sum**: Multiply these weights by their corresponding Value vectors and sum them up to get the final self-attention output.

$$Attention(Q,K,V)=Softmax(\frac{QK^{T}}{\sqrt{d_k}})V$$
#### 3.3 Multi-Head Attention

**Motivation**

Using only one set of Q, K, V might limit the model's ability to focus on information from different perspectives. For example, one head might focus on syntactic relationships, while another focuses on semantic relationships.

**Implementation**

* Linearly project (split) the original Q, K, V vectors into h smaller pieces along the dimension axis (h is the number of heads).
* Perform parallel self-attention calculations on each of these h sets of Q, K, V, resulting in h output matrices.
* Concatenate these h output matrices back together.
* Pass the concatenated matrix through a final linear layer to produce the final output.

#### 3.4 Position-wise Feed-Forward Network - FFN

This is a simple fully connected feed-forward network that is applied to each position (i.e., each word's representation vector) separately and identically.

* It consists of two linear transformations with a ReLU activation function in between

$$FFN(x)=max(0,xW_1+b_1)W_2+b_2$$

**Purpose**

It adds non-linearity to the model and allows for more complex transformations and combinations of the features extracted by the self-attention layer.

#### 3.5 Masking in the Decoder

**Goal**

During the decoding (generation) phase, when predicting the t-th word, the model should only see the words generated before position t, not any future words. This is known as the "auto-regressive" property.

**Implementation**

In the first self-attention layer of the decoder (Masked Multi-Head Self-Attention), before applying Softmax, we set the attention scores for all future positions to a very large negative number (e.g., −∞). After the Softmax operation, the weights for these positions become 0, effectively "masking" future information.

***
### 4.Training

**Loss Function**

* Cross-Entropy Loss is typically used.

**Optimizer**

* The paper uses the Adam optimizer with a special learning rate scheduler. It linearly increases the learning rate during an initial "warmup" phase and then decreases it proportionally to the inverse square root of the step number.
