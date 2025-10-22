### 1.Token Embedding

**Purpose**

>To convert individual tokens (words, subwords, or characters) into dense vector representations that capture their semantic meaning

**Importance**

>Models cannot directly process raw text. Token embeddings map the discrete, symbolic representation of language (like a word's ID from a vocabulary) into a continuous vector space where semantically similar tokens are located closer to each other. This is the foundational layer for understanding the content of the text.

**How it works**

>It is typically implemented as a large lookup table or an "embedding layer". The vocabulary size determines the number of rows in the table, and the embedding dimension (e.g., 768 in BERT-Base) determines the number of columns. When a token ID is input, the layer simply retrieves the corresponding row (vector). These vectors are initialized randomly and are learned and updated during the model training process.

***
### 2.Positional Embedding

**Purpose**

>To provide the model with information about the order of tokens in a sequence

**Importance**

>The core mechanism of the Transformer, the self-attention mechanism, is permutation-invariant. This means it processes all tokens simultaneously without any inherent knowledge of their positions. Without positional information, "the cat sat on the mat" and "the mat sat on the cat" would look identical to the model. Positional embeddings inject this crucial sequential context.

**How it works**

* **Sinusoidal (Sine/Cosine) Functions:** Used in the original Transformer. It uses a fixed formula based on sine and cosine functions of different frequencies to generate a unique positional vector for each position. This method has the advantage of being able to generalize to sequences longer than those seen during training
* **Learned Positional Embeddings:** Used in BERT, GPT, and ViT. This is a simpler approach where the positional embedding is just another lookup table, similar to token embeddings. A vector is learned for each possible position (up to a maximum sequence length, e.g., 512 in BERT). These embeddings are initialized randomly and learned during training.

***
### 3.Segment Embedding

**Purpose**

>To help the model distinguish between different sentences or segments within the same input sequence.

**Why is it needed**

>This is particularly important for pre-training tasks like Next Sentence Prediction (NSP) in BERT, or for any downstream task that requires understanding the relationship between two sentences (e.g., Question Answering, Natural Language Inference). The model needs a clear signal to know which token belongs to which sentence.

**How it works**

>It is also a learned embedding, but the "vocabulary" is very small. Typically, there are only two segment embeddings: one for the first sentence (Segment A) and one for the second sentence (Segment B). For every token in the first sentence, the Segment A embedding is added. For every token in the second sentence (and the `[SEP]` token separating them), the Segment B embedding is added.