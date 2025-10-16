### 1.Basic Component

>The most fundamental component of a neural network is the "neuron" (also called a unit) model

### 2.M-P Neuron Model

>This is a simple model that is still widely used today. It receives input signals from other neurons, which are transmitted through weighted connections. The total input received by a neuron is compared with a threshold, and then processed by an "activation function" to produce the neuron's output.

$$y=f(\sum^{n}_{i=1}w_{i}x_{i}-\theta)$$
### 3.Activation Function

* The ideal activation function is the step function, but its discontinuity and lack of smoothness make it less practical.
* In practice, the Sigmoid function is often used. It squashes inputs from a large range into a (0,1) range, which is why it's also called a "squashing function"

![](../4.Neural%20Networks/images/sigmoid.png)
