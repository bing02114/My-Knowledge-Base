### 1.Encoder-Decoder Architecture

#### 1.1 Structure

* It consists of two main parts: an **Encoder** stack and a **Decoder** stack.
* **Encoder:** Processes the entire input sequence at once, building a rich, context-aware representation of it. It uses a bidirectional self-attention mechanism where every token can attend to every other token in the input.
* **Decoder:** Generates the output sequence one token at a time (auto-regressively). It has two types of attention mechanisms: a masked self-attention to look at the previously generated output tokens, and a cross-attention mechanism to look at the encoder's output representation.

#### 1.2 How it Works

* The Encoder reads the entire source sequence (e.g., an English sentence).
* It generates a set of context vectors (representations) for the source sequence
* The Decoder takes these context vectors and begins generating the target sequence (e.g., the French translation) token by token, using the information from both the source sentence and what it has already generated.

#### 1.3 Best For

* Sequence-to-sequence tasks where the input and output can have different lengths and structures.
* **Examples:** Machine Translation, Text Summarization, Question Answering.

#### 1.4 Example Models

* Original Transformer, T5, BART

***
### 2.Encoder-Only Architecture

#### 2.1 Structure

* Consists solely of the Transformer's Encoder block.
* It processes the input text bidirectionally, meaning each token's representation is built by considering both the text that comes before it and the text that comes after it simultaneously.

#### 2.2 How it Works

* The model takes an input sequence (often with some tokens masked for training).
* It passes the sequence through multiple layers of bidirectional self-attention and feed-forward networks
* The final output is a high-quality numerical representation for each input token, deeply infused with context from the entire sequence. This representation can then be used by adding a simple classification layer on top for various downstream tasks

#### 2.3 Best For

* Tasks that require a deep, holistic understanding of the input text. (NLU - Natural Language Understanding tasks).
* **Examples:** Sentiment Analysis , Named Entity Recognition (NER), Sentence Classification.

#### 2.4 Example Models

* BERT and its variant

***
### 3.Decoder-Only Architecture

#### 3.1 Structure

* Consists solely of the Transformer's Decoder block (minus the cross-attention layer).
* It is **auto-regressive** or **causal**, meaning it processes text in a strict left-to-right order. When predicting the token at position `i`, the model can only see the tokens from position `0` to `i-1`. This is enforced by a masked self-attention mechanism.

#### 3.2 How it Works

* The model takes a starting sequence of text (a "prompt").
* It passes this prompt through its layers to predict the most likely next token
* This predicted token is then appended to the sequence, and the process repeats to generate the next token, and so on, creating a continuous stream of text

#### 3.3 Best For

* Text generation tasks. (NLG - Natural Language Generation tasks).
* **Examples:** Open-ended text generation , Dialogue systems , Creative Writing (创意写作), Code Generation .

#### 3.4 Example Models

* GPT series
