### 1.From Linear Models to Neural Networks
#### 1.1 From GLM to a Single Neuron

* A single neuron can be seen as an extension of a GLM
* The "link function" is replaced by an "activation function"
* The basic expansion becomes an affine transformation (linear transformation plus a bias term)

**Neuron Output Formula**

$$y=\sigma(b+\sum_{i}\theta^{T}_{i}x_{i})$$
* This formula represents a weighted sum of inputs plus a bias, passed through a non-linear activation function

#### 1.2 Stacking Neurons: Multi-Layer Perceptron (MLP)

* Multiple neurons can be stacked together to form a layer. The output of this layer is a vector
* For a single layer with weight matrix W and bias vector b, the output is:

$$y=\sigma(Wx+b)$$

* By stacking multiple layers, we create a deep neuron network or Multi-Layer Perceptron (MLP)
* A 1-hidden-layer MLP is defined as

$$y=\sigma(W^{(1)}\sigma(W^{(0)}x+b^{(0)})+b^{(1)})$$

* An MLP can be viewed as **a parameterized basis expansion**, where the network learns the optimal features instead of them being manually engineered

***
### 2.Training Neural Network

#### 2.1 Gradient Descent

* Neural networks are trained by iteratively adjusting their parameters to minimize a loss function

**Update Rule**

$$\theta^{(i+1)}=\theta^{(i)}-\alpha \nabla_{\theta}L(\theta^{(i)})$$
* Where $\alpha$ is the learning rate and $\nabla_{\theta}L$ is the gradient of the loss with respect to the parameteres

#### 2.2 The Challenge of Gradient Computation

* Calculating the gradient for a deep network involves extensive use of the chain rule, which can be very complex to do by hand
* Numerical approximation is an alternative, but it's computationally expensive and introduces approximation errors that can compound

***
### 3.Automatic Differentiation

>Automatic Differeentiation is a technique to compute exact derivatives programmatically by breaking down complex functions into a sequence of elementary operations

#### 3.1 Forward Mode AD

**Idea**: It computes the derivative by propagating it forward through the computation graph, from inputs to outputs. It calculates how a small change in one input affects all intermediate variables and the final output.

**Process**: It tracks both the `value` and the `derivative` (called a "dual number") for each variable at every step of the computation

**Complexity**: 

$$O(nT)$$

where `n` is the number of input parameters and `T` is the complexity of the forward pass. It computes one column of the Jacobian matrix at a time

**Use Case**: Efficient when the number of inputs (n) is much smaller than the number of outputs (m).

