### 1.The Problem with Standard RNNs

Standard RNNs are designed to work with sequential data. They have a "memory" in the form of a hidden state that is updated at each timestep, theoretically allowing them to retain information from past inputs.

However, in practice, RNNs suffer from the **vanishing and exploding gradient problems**. When training with backpropagation through time, the gradients can shrink exponentially as they are propagated back through many timesteps. This means the network cannot learn the influence of early inputs on later outputs, making it incapable of capturing **long-term dependencies**. For example, in the sentence "The clouds are in the _sky_," the model needs to remember "clouds" to predict "sky," which is a short-term dependency. But in "I grew up in France... therefore, I speak fluent _French_," the model needs to remember "France" from much earlier, which is a long-term dependency. Standard RNNs struggle with the latter.

***
### 2.The LSTM Solution: Gates and a Cell State

LSTMs were specifically designed to solve this problem. The core innovation of an LSTM is its **cell state (Ct​)** and a series of **gates (门)** that regulate the flow of information into and out of this state

**Cell State (Ct​)**: Think of this as the model's long-term memory. It runs straight down the entire chain of the network, with only minor linear interactions. Information can be added to or removed from the cell state, which is controlled by the gates.

**Gates**: These are neural network layers (typically with a sigmoid activation function) that learn which information is important to keep or discard. A sigmoid function outputs a value between 0 and 1, representing how much of each component should be let through (0 means "let nothing through," 1 means "let everything through").

An LSTM cell has three main gates: the **Forget Gate**, the **Input Gate**, and the **Output Gate**.

***
### 3.The Internal Mechanism of an LSTM Cell

#### 3.1 The Forget Gate

The first step is to decide what information to throw away from the long-term memory (the cell state Ct−1​). This decision is made by the forget gate.

**Function:** It looks at ht−1​ and xt​ and outputs a number between 0 and 1 for each number in the cell state Ct−1​. A 1 represents "completely keep this," while a 0 represents "completely get rid of this."

$$f_{t}=\sigma(W_{f}·[h_{t}-1,x_{t}]+b_{f})$$

#### 3.2 The Input Gate

The next step is to decide what new information we’re going to store in the cell state. This has two parts.

1. **Which values to update?** The input gate (a sigmoid layer) decides which parts of the new information are important
2. **What new values to add?** A `tanh` layer creates a vector of new candidate values, C~t​, that could be added to the state

**Function**

The input gate determines which pieces of the candidate information C~t​ are actually added to the long-term memory.

**Formulas**

$$i_{t}=\sigma(W_{i}·[h_{t}-1,x_t]+b_{i})$$

#### 3.3 Updating the Cell State

Now we can update the old cell state, Ct−1​, into the new cell state, Ct​.

**Function**

We multiply the old state by ft​ (forgetting the things we decided to forget) and then add it​∗C~t​ (the new candidate values, scaled by how much we decided to update each state value).

$$C_{t}=f_{t}·C_{t}-1+i_{t}·\widetilde{C}_{t}$$
#### 3.4 The Output Gate

Finally, we need to decide what our output is going to be. This output will be the new hidden state, ht​.

**Function**

The output gate decides which parts of the cell state we are going to output. First, we run a sigmoid layer which decides which parts of the cell state to output. Then, we put the cell state through `tanh` (to push the values to be between -1 and 1) and multiply it by the output of the sigmoid gate.

$$\sigma_{t}=\sigma(W_{o}·[h_{t}-1,x_{t}]+b_o)$$

***
### 4.Advantages of LSTM 

**Captures Long-Term Dependencies:** The gating mechanism and the separate cell state allow the network to effectively remember information over long sequences

**Mitigates Vanishing/Exploding Gradients:** The additive nature of the cell state update (Ct​=...+...) and the gating mechanism ensure that gradients can flow much more effectively through time without vanishing or exploding

