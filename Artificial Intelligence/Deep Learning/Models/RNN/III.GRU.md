### 1.Motivation for GRU

The GRU was introduced in 2014 by Kyunghyun Cho et al. as a simpler alternative to the LSTM. Like LSTM, its primary goal is to solve the **vanishing gradient problem** that affects standard RNNs, thereby enabling the model to capture **long-term dependencies**. The key idea behind GRU is to achieve this with a simpler architecture and fewer parameters than LSTM, which can lead to faster training times and require less data to generalize well.

***
### 2.The GRU Solution: Two Gates, No Cell State

The most significant difference between GRU and LSTM is its architecture. GRU merges the **cell state** and **hidden state** into a single hidden state vector, ht​. It also combines the forget and input gates of an LSTM into a single **Update Gate** and introduces a new **Reset Gate**.

* **Update Gate (zt​):** This gate acts similarly to the combination of the forget and input gates in an LSTM. It decides how much of the past information (the previous hidden state ht−1​) should be kept and how much of the new candidate information should be added.
* **Reset Gate (rt​):** This gate is used to decide how much of the past information to _forget_ when creating the new candidate hidden state. If the reset gate is close to 0, it essentially makes the cell act as if it's reading the first input of a sequence, allowing it to forget the previously computed state

***
### 3.The Internal Mechanics of a GRU Cell

#### 3.1 The Reset Gate

>It controls how much of the past memory contributes to the calculation of the new candidate memory.

$$r\_t=\sigma(W\_r·[h_{t}-1,x_t]+b_r)$$

#### 3.2 The Update Gate

>It balances between the old memory and the new information

$$z\_t=\sigma(W\_z·[h\_t-1,x\_t]+b\_z)$$

#### 3.3 Calculating the Candidate Hidden State

>It creates a new piece of information based on the current input and a _reset_ version of the previous hidden state. The element-wise product rt​⋅ht−1​ determines which parts of the past information are erased before calculating the new candidate state

$$\widetilde{h}*t=tanh(W_{h}·[r_t·h*t-1,x_t]+b_h)$$

#### 3.4 Calculating the Final Hidden State

>Finally, the new hidden state, ht​, is computed by interpolating between the previous state, ht−1​, and the candidate state, h~t​, using the update gate, zt​.
>
>It explicitly determines what to keep from the old state and what to add from the new candidate state. The term (1−zt​) controls what is forgotten from the past, while zt​ controls what new information is added

$$h_t=(1-z_t)h_t-1+z_t·\widetilde{h}_t$$





