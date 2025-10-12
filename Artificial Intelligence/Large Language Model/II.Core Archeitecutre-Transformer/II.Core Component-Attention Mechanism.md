### 1.Attention



***
### 2.Multi-Head Attention
#### 2.1 Definition

>**Multi-Head Attention** is a mechanism in the Transformer model that runs the attention process multiple times in parallel and then combines the results. Instead of calculating attention once, it splits the model's inputs into several "heads," allowing each head to learn different aspects of the information.
>
>The core idea is that it allows the model to jointly attend to information from different representation subspaces at different positions. A single attention head might be limited to focusing on one type of relationship, but multiple heads can capture a richer set of relationships (e.g., syntactic, semantic, positional).

#### 2.2 Mechanism

**Step 1: Linear Projections**

>The initial Query (Q), Key (K), and Value (V) vectors are fed through separate linear layers and split into h smaller pieces. Each of these pieces becomes the Q, K, and V for one attention head.
>
>The input embedding of dimension is going to be divided
>
>$$d_{k}=d_{v}=d_{model}/h$$

**Step 2: Parallel Attention Calculation**

>The **Scaled Dot-Product Attention** mechanism is applied to each of the h sets of (Q, K, V) in parallel. This produces h separate output vectors, one for each head.

**Step 3: Concatenation**

>The output vectors from all h heads are concatenated together into a single, large vector. 
>
>The dimension of this concatenated vector will be h×dv​, which equals the original input dimension, d_model​.

**Step 4: Final Linear Projection**

>The concatenated vector is passed through one final linear layer (with weight matrix WO) to produce the final output of the Multi-Head Attention block. 
>
>This layer allows the model to learn how to best combine the information learned by the different heads.


### 2.3 Meaning

- **Learning Different Relationships:** 
	
	- A single attention mechanism might average all the information together, potentially missing specific nuances. Multiple heads allow the model to learn different types of relationships simultaneously. For example, one head might learn to track long-range dependencies, while another focuses on local syntactic relationships.
	
- **Richer Representations:** 
	
	- Each head operates in a different "representation subspace" (due to the initial linear projections). This provides the model with a richer, more diverse set of features from the input, leading to a more powerful representation.
	
- **Increased Model Capacity:** 
	
	- It increases the model's capacity to capture complex patterns without significantly increasing the computational cost compared to using a single, very large attention mechanism.