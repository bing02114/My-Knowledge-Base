### 1.Concept

>A typical deep learning model is a very deep neural network with multiple hidden layers. Increasing the number of hidden layers is more effective for increasing model complexity than increasing the number of neurons in a single hidden layer

### 2.Training Method

>Training deep networks is challenging because errors can "diverge" during backpropagation. Unsupervised layer-wise training is an effective technique.

* **Pre-training**: Each layer is trained one at a time in an unsupervised manner, with the output of the previous layer serving as the input for the current one. For example, a Deep Belief Network (DBN) is a stack of RBMs trained this way.
* **Fine-tuning**: After pre-training, the entire network is fine-tuned using a supervised algorithm like BP

### 3.Weight Sharing

>A strategy where a group of neurons uses the same set of connection weights. This is a crucial element of Convolutional Neural Networks (CNNs).

### 4.Feature Learning

>Deep learning can be seen as a process of "feature learning" or "representation learning." It transforms the initial data representation through multiple layers, converting it into a representation that makes tasks like classification easier. This reduces the need for manual "feature engineering."