>A Tokenizer is a crucial component in the Natural Language Processing (NLP) pipeline. Its primary job is to convert raw text into a sequence of numerical inputs (Token IDs) that a model can understand. This process involves two main steps: tokenizing the text into tokens (sub-units like words or subwords) and then converting these tokens into their corresponding IDs from a vocabulary.

### 1.Tokenization Strategies

>The choice of tokenization strategy directly impacts the model's performance, vocabulary size, and ability to handle unknown words.

#### 1.1 Word-level

**Description**

>This is the most intuitive strategy. It splits text based on spaces and punctuation. Each word becomes a token

**Advantages**

>**Semantically Meaningful:** Each token is a complete word with clear meaning
>
>**Conceptually Simple:** Easy to implement and understand

**Disadvantage**

>**Huge Vocabulary Size:** The vocabulary can become extremely large for languages with rich morphology (e.g., English, German), requiring significant memory.
>
>**Out-of-Vocabulary (OOV) Problem:** The model cannot handle words that were not in the training data (e.g., typos, new words, names). These are mapped to an `[UNK]` token, leading to information loss

#### 1.2 Character-level

**Description**

>This strategy splits text into its individual characters.

**Advantages**

>**Very Small Vocabulary:** The vocabulary size is very small, consisting of all possible characters (e.g., letters, numbers, punctuation)
>
>**No OOV Problem:** There are no "unknown" characters, so it can handle any word

**Disadvantages**

>**Extremely Long Sequences:** It creates very long token sequences, increasing computational cost and memory requirements
>
>**Loss of Semantic Meaning:** Individual characters carry very little semantic information, making it harder for the model to learn meaningful representations.

#### 1.3 Subword-level

>This is the most common and effective strategy used in modern language models. It balances the pros and cons of word-level and character-level tokenization. The core idea is to keep frequent words as single tokens while splitting rare words into smaller, meaningful subword units.

**Advantages of Subword Tokenization**

>**Manages Vocabulary Size:** It controls the vocabulary size, keeping it reasonable
>
>**Handles OOV Words:** It can represent rare or unknown words by breaking them down into known subwords, effectively eliminating the OOV problem.
>
>**Captures Morphological Information:** It can understand relationships between words like "learn", "learning", and "learner" because they share the same root subword "learn".

**a) BPE (Byte Pair Encoding)**

>It's a data compression algorithm adapted for tokenization. It starts with a vocabulary of individual characters and iteratively merges the most frequent adjacent pair of tokens until the desired vocabulary size is reached.

**b) WordPiece**

>It's very similar to BPE, but the merge criterion is different. Instead of merging the most frequent pair, WordPiece merges the pair that maximizes the likelihood of the training data once merged. In practice, this tends to create subwords that are more meaningful. It often marks subwords that are not at the beginning of a word with a `##` prefix.

**c) Unigram**

>This approach is probabilistic and works in the opposite direction of BPE and WordPiece. It starts with a large vocabulary (e.g., all pre-tokenized words and many subwords) and iteratively removes tokens that are least likely to be needed, based on a Unigram language model, until the vocabulary shrinks to the desired size. When tokenizing, it finds the most probable segmentation of a word into subwords.

***
### 2.Special Tokens

| **Token**   | **Name (名称)**      | **Purpose (目的)**                                                                                                                                                                         | **Example (示例)**                                            |
| ----------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| **`[CLS]`** | **Classification** | Placed at the beginning of a sequence. Its final hidden state is used as the aggregate representation for classification tasks. (置于序列的开头。其最终的隐藏状态被用作整个序列的聚合表示，用于分类任务。)                   | `[CLS] The cat sat on the mat. [SEP]`                       |
| **`[SEP]`** | **Separator**      | Used to separate two sentences for tasks like Question Answering or Natural Language Inference. It also marks the end of a single sequence. (用于分隔两个句子，以完成问答或自然语言推断等任务。它也用作单个序列的结束标记。)    | `[CLS] Sentence A. [SEP] Sentence B. [SEP]`                 |
| **`[PAD]`** | **Padding**        | Used to pad shorter sequences in a batch to the same length as the longest sequence. This is necessary for efficient batch processing. (用于将批处理（batch）中较短的序列填充到与最长序列相同的长度。这对于高效的批处理是必需的。) | `[CLS] A short sentence. [SEP] [PAD] [PAD]`                 |
| **`[UNK]`** | **Unknown**        | Represents a token that is not in the tokenizer's vocabulary. Subword tokenizers greatly reduce the need for this token. (代表一个不在分词器词汇表中的词元。子词分词策略极大地减少了对这个词元的需求。)                        | `[CLS] I saw a xzzz. [SEP]` -> `[CLS] I saw a [UNK]. [SEP]` |