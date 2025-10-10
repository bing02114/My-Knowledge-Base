### 1.Sigmoid Function

$$\sigma(x)=\frac{1}{1+e^{-x}}$$

**Output Range**: (0,1)

**Properties**

>It squashes any real-valued number into a range between 0 and 1. It is **differentiable** and has a smooth "S"-shaped curve.

**Use Cases**

>Primarily used in the output layer of a **binary classification** model to represent a probability.

**Disadvantages**

>* **Vanshing Gradients**
>* **Not Zero-Centered**
>* **Computationally Expensive**>

### 2.Tanh (Hyperbolic Tangent) Function

$$tanh(x)=\frac{e^{x}-e^{-x}}{e^{x}+e^{-x}}$$

**Output Range**: (-1,1)

**Properties:**

>Similar to Sigmoid but its output is **zero-centered**. This makes it generally preferred over Sigmoid for **hidden layers** in earlier neural networks.

**Disadvantages**

>It still suffers from the **vanishing gradient problem** for large positive or negative values.

### 3.ReLU (Rectified Linear Unit) Function

$$f(x)=max(0,x)$$

**Output Range**: [ 0 , ∞ ]

**Properties**

>It is a very simple and computationally efficient function. It outputs the input directly if it is positive, and 0 otherwise. 
>
>**It has become the default activation function for hidden layers in most neural networks.**

**Advantages:**

>* **Solving Vanishing Gradient**
>* **Sparsity**
>* **Fast Computation**

**Disadvantages**:

>* **Dying ReLU Problem**
>* **Not Zero-Centered**

### 4.Leaky ReLU

$$ 
f(x)=\left\{
\begin{matrix}
 x & {if~x>0}\\
 ax & \text{otherwise}
\end{matrix} 
\right.
$$

**Properties**

>Leaky ReLU is an attempt to fix the "Dying ReLU" problem. Instead of being 0 for negative inputs, it has a small negative slope (α).

**Advantage**

>It allows for a small, non-zero gradient when the unit is not active, **preventing the neuron from dying.**

### 5.Softmax Function

$$Softmax(x_i)=\frac{e^{x_i}}{\sum^{K}_{j=1}e^{x_j}}$$

**Output Range**

>(0, 1) for each element, and the sum of all elements is 1.

**UseCases**

>Used exclusively in the output layer of a **multi-class classification** model. It converts a vector of raw scores (logits) into a probability distribution over the different classes.

**Properties**

>The output can be interpreted as the model's confidence or probability for each class. The class with the highest probability is the model's final prediction.