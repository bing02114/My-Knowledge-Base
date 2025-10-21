>The primary motivation for these layers is to address a problem called **Internal Covariate Shift**. As the weights in earlier layers of a network change during training, the distribution of the inputs to deeper layers also changes. This constant shifting of distributions makes it difficult for the deeper layers to learn effectively. Normalization layers help by standardizing the inputs to each layer, which stabilizes and accelerates the training process.

### 1.Batch Normalization - CNN

**Core Idea** : It normalizes the activations of a layer for each feature/channel **across the mini-batch**. For a given feature, it calculates the mean and variance of that feature over all samples in the current mini-batch.

**How it Works**: 

1. For a feature map (channel), calculate the mean ($μ_B$​) and variance ($σ_{B}^{2}$​) across all samples in the mini-batch
2. Normalize the activations: $\hat{x_{i}}=\frac{x_{i}-\mu_B}{\sqrt{\sigma^{2}_{B}+\epsilon}}$
3. Scale and shift the normalized values : $y_{i}=\gamma \hat{x_{i}}+\beta$

**Properties**

**Learnable Parameters:** BN introduces two learnable parameters per feature, **gamma (γ)** for scaling and **beta (β)** for shifting. This allows the network to learn the optimal scale and mean for the activations, essentially giving it the ability to "undo" the normalization if that's what the network needs.

**Batch Size Dependent:** Its performance is heavily dependent on the batch size. It requires a sufficiently large batch size to estimate the feature statistics accurately. It performs poorly with small batch sizes (e.g., 1, 2, 4).

**Different Behavior in Training vs. Inference:** During training, it uses the statistics of the current mini-batch. During inference, it uses a running average of the mean and variance collected during the entire training process

**Regularization Effect:** Because the statistics are calculated on a noisy mini-batch, it adds a slight regularization effect, which can sometimes reduce the need for Dropout.

***
### 2.Layer Normalization (LN) - RNN / Transformer

**Core Idea**: It normalizes the activations **within a single training example** across all of its features/channels. It does not depend on the batch dimension at al

**How it Works**

1. For a single sample, calculate the mean (μL​) and variance (σL2​) across all of its features.
2. Normalize, scale, and shift, similar to BN.

**Properties**

**Batch Size Independent:** Since the calculation is done per-sample, its performance is independent of the batch size. This makes it ideal for RNNs where sequence lengths can vary and for models that require small batch sizes due to memory constraints (like Transformers).

**Same Behavior in Training vs. Inference:** The calculation method is identical during both training and inference, making it simpler to implement.

**Dominant in NLP:** It is the standard normalization layer for Transformers (e.g., BERT, GPT) and other modern NLP architectures

***
### 3.Instance Normalization

Instance Normalization can be seen as a middle ground between Batch Norm and Layer 
Norm.

**Core Idea** : It normalizes the activations **per channel, per sample**. For a CNN, this means it calculates the mean and variance for each feature map (channel) individually for each sample in the batch

**Properties**

**Batch Size Independent:** Like LN, it is independent of the batch size

**Removes Instance-Specific Contrast:** By normalizing per channel for a single image, it effectively removes style information related to contrast and color. This property makes it extremely effective for **style transfer** tasks, where the goal is to separate the content of an image from its style.

**Primary Use Case:** Neural Style Transfer and other generative tasks where style manipulation is important.

***
### 4.Group Normalization

**Core Idea**: It is a hybrid of Layer Norm and Instance Norm. It divides the channels into a number of **groups** and then performs normalization **per sample, per group**

**Properties**

- **Batch Size Independent:** It is not dependent on the batch size.
    
- **Flexible and General:** It can be seen as a general form of normalization. If the number of groups is 1, it becomes Layer Normalization. If the number of groups equals the number of channels, it becomes Instance Normalization. 
    
- **A Good General Alternative to BN:** GN provides stable performance across a wide range of batch sizes and has been shown to be a strong alternative to BN, especially when training with small batches is necessary (e.g., in object detection or segmentation tasks with high-resolution images). 



