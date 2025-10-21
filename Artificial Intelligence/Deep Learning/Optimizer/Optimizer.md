### 1.SGD

- **Properties:** 
    
    - SGD randomly selects only one sample in each iteration to compute the gradient and update the parameters.
        
- **Advantages:**
    
    - Fast update speed and low computational cost
        
    - The randomness of the gradients helps to escape local optima and potentially find a better optimal solution.
        
- **Disadvantages:**
    
    - Since only one sample is used at a time, the variance of the gradient estimate is very large, leading to a highly unstable and fluctuating loss function during descent.
        
    - Convergence can be slow because it does not head directly towards the optimal solution.

***

### 2.Adagrad (Adaptive Gradient Algorithm)

**Properties**

It maintains a separate learning rate for each parameter. The learning rate for frequently updated parameters becomes very small, while the learning rate for infrequently updated parameters remains relatively large.

**Advantages**

It performs very well in sparse data scenarios, such as word embeddings in natural language processing

No need to manually tune the learning rate

**Disadvantages**

Its learning rate monotonically decreases as training progresses, eventually becoming so small that the model stops learning prematurely

***
### 2.RMSprop (Root Mean Square Propagation)

**Properties**

>Similar to Adadelta, RMSprop also aims to solve the problem of Adagrad's rapidly decreasing learning rate. It uses an exponential moving average of the gradients to adjust the learning rate.

**Advantage**

It performs well on non-stationary objectives

It has been proven to be an effective and practical optimization algorithm in practice

***
### 3.Adam

**Properties**

>Adam is arguably one of the most popular and widely used optimizers today. It combines the ideas of Momentum and RMSprop. It uses both the first-moment estimate of the gradient (like Momentum) and the second-moment estimate (like RMSprop) to dynamically adjust the learning rate for each parameter.

**Advantages**

* Computationally efficient and requires little memory
* Has individual learning rates for different parameters.
* Performs well in a wide variety of deep learning models and is often the default choice

**Disvantages**

In some cases, it may fail to converge to an optimal solution. Some research suggests that a well-tuned SGD with Momentum can sometimes outperform Adam on certain tasks

