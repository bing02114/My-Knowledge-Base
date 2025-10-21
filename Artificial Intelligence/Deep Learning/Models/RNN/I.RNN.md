### 1.Definition

>A **Recurrent Neural Network (RNN)** is a type of artificial neural network designed to recognize patterns in sequences of data, such as text, speech, or time-series data. Unlike standard feedforward networks, RNNs have a "memory" which allows them to use information from prior inputs to influence the current input and output.
>
>The defining feature of an RNN is its **recurrent loop**. This loop allows information to persist by feeding the output of a neuron back into itself for the next step in the sequence.

### 2.The Core Architecture

![](Artificial%20Intelligence/Deep%20Learning/images/RNN.png)
$$h_t=tanh(UX_t+Vh_{t-1}+b_h)$$

$$L_t=softmax(Wh_t+b_L)$$

>An RNN processes a sequence one element at a time. 
>
>At each timestep t, the network takes two inputs: the current input data xt​ and the hidden state from the previous timestep, h_{t−1}​.

**Hidden State**

>This is the "memory" of the network. It's a vector that captures information about what has happened in all the previous timesteps. The hidden state ht​ is calculated based on the previous hidden state ht−1​ and the current input xt​.

**Output**

>At each timestep, the network can also produce an output yt​, which is typically calculated from the current hidden state ht​.

>**The same set of weights (W, U, V) are used for every timestep, which makes the model efficient and allows it to generalize across sequences of different lengths.**



### 3.Applications

>RNNs are well-suited for tasks involving **sequential** **data**.

**NLP**

>Language modeling, machine translation, sentiment analysis, text generation.

**Speech Recognition**

>Converting audio sequences into text.

**Time-Series Prediciton**

>Forecasting stock prices, weather, or any data that evolves over time.

**Video Analysis**

>Classifying activities in sequences of video frames.


### 4.Challenges and Limitations

**Vanishing and Exploding Gradient Problems**

>The primary challenge in training RNNs. When backpropagating through many timesteps, **the gradients can either shrink exponentially to zero (vanish) or grow exponentially to infinity (explode).**

**Vanishing Gradients**

>make it very difficult for the model to learn long-range dependencies—it "forgets" information from the distant past.

**Short-Term Memory**

>Due to the vanishing gradient problem, simple RNNs struggle to retain information over long sequences.

**Solutions**

>These limitations led to the development of more advanced recurrent architectures like **Long Short-Term Memory (LSTM)** and **Gated Recurrent Unit (GRU)**, which were specifically designed to combat the vanishing gradient problem and better capture long-range dependencies.
