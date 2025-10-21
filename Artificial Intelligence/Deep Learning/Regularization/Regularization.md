### 1.L1 & L2 Regularization

#### 1.1 Core Idea

>A model with large weights is considered more complex. By penalizing large weights, we encourage the model to find simpler solutions that generalize better.

#### 1.2 L2 Regularization (Weight Decay or Ridge)

$$L_{new}=L_{original}+\lambda \sum_{i}w_{i}^{2}$$

>It encourages the weight values to be small and distributed evenly. It effectively "decays" the weights towards zero but rarely makes them exactly zero. It is the most common type of weight regularization

#### 1.3 L1 Regularization (Lasso)

$$L_{new}=L_{original}+\lambda \sum_{i}|w_{i}|$$

>L1 regularization can push some weight values to be _exactly_ zero. This leads to a **sparse model**, meaning some features are completely ignored. It can be useful for feature selection, but in deep learning, L2 is generally preferred

***
### 2.Dropout

#### 2.1 Core Idea

>To prevent neurons from co-adapting too much with each other. If neurons know that their inputs might randomly disappear, they learn to be more robust and to detect features on their own

#### 2.2 How it Works

>During training, for each forward pass, a fraction of the neurons in a layer are randomly "dropped out" or deactivated. This means they are temporarily ignored: their output is set to zero, and they don't participate in the backpropagation step. The choice of which neurons to drop is random for each mini-batch.

#### 2.3 Why it Works

**Ensemble Effect:** Training a network with dropout is like training an exponential number of smaller, different neural networks simultaneously. At test time, all neurons are used, which is like averaging the predictions of this large ensemble of networks

**Forces Robust Features:** A neuron cannot rely on the presence of any single other neuron. It must learn features that are useful in many different contexts, making the model more robust