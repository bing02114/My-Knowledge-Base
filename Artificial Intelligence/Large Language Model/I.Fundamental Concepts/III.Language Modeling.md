### 1.Causal Language Model

>Also known as an auto-regressive model. This is a traditional and intuitive form of language modeling

**Core Idea**

>Left-to-right prediction of the next word

* The model's task is to predict the next token in a sequence, given all the preceding tokens. It processes text in one direction only (typically left-to-right). This is why it's called "causal" – the prediction of a word is only caused by the words that came before it, not after.

**Mathematical Representation**

>It models the joint probability distribution of a sequence P(w1​,w2​,...,wn​) by factorizing it into a product of conditional probabilities:

$$P(w_1,\dots,w_n)=\prod^{n}_{i=1}P(w_i|w_1,\dots,w_{i-1})$$

**Example Model**

* GPT series

**Strengths and Use Cases**

* **Excellent for Text Generation:** Because its pre-training objective is to generate the next word, it excels at tasks like open-ended text generation, story writing, dialogue systems, and summarization.
* It naturally produces coherent and fluent text
***
### 2.Masked Language Model

>Also know as a denoising auto-encoder model. This approach was popularized by BERT and revolutionized the field of text understanding

**Core Idea**

>Fill-in-the-blanks

* Instead of predicting the next word, the model is trained to predict randomly masked (hidden) tokens in a sequence. During pre-training, a certain percentage of the input tokens (e.g., 15%) are replaced with a special `[MASK]` token. The model's goal is to predict the original identity of these masked tokens.

**How it works**

* Unlike Causal LM, a Masked LM can look at the entire sequence—both left and right context—to predict the masked word. This is why it's called **bidirectional**.

**Example Model**

* BERT series

**Strengths and Use Cases**

* **Excellent for Text Understanding:** By learning to use both left and right context, Masked LMs build deep, rich, bidirectional representations of language. They are superior for tasks that require a holistic understanding of the entire sentence.
* Typical applications include sentiment analysis, question answering, named entity recognition (NER), and sentence classification. They are often used as powerful feature extractors.