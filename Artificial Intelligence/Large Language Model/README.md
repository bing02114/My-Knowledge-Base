# Core Concepts of Large Language Models (LLM)

## I. Fundamental Concepts

### Tokenizer

- **Tokenization Strategies**
    
    - Word-level
        
    - Character-level
        
    - **Subword-level**
        
        - BPE (GPT series)
            
        - WordPiece (BERT series)
            
        - Unigram (T5)
            
- **Special Tokens**
    
    - `[CLS]`, `[SEP]`, `[PAD]`, `[UNK]`
        

### Embedding

- Token Embedding
    
- **Positional Embedding**
    
- Segment Embedding
    

### Language Modeling

- **Causal Language Model (Causal LM)**
    
    - GPT series
        
    - "Left-to-right" prediction of the next word
        
- **Masked Language Model (Masked LM)**
    
    - BERT series
        
    - "Fill-in-the-blanks"
        

***
## II. Core Architecture: Transformer 

### Overall Structure

- Encoder-Decoder Architecture
    
- Encoder-Only (BERT)
    
- Decoder-Only (GPT)
    

### Core Component: Attention Mechanism

- **Self-Attention**
    
    - **Q, K, V (Query, Key, Value)**
        
    - Scaled Dot-Product Attention
        
- **Multi-Head Attention**
    
- **Attention Mechanism Optimizations**
    
    - **MQA (Multi-Query Attention)**
        
    - **GQA (Grouped-Query Attention)**
        

### Other Key Modules

- Feed-Forward Network (FFN)
    
- Residual Connection
    
- Layer Normalization
    

***
## III. Key Technologies & Optimizations 

### Training

- **Pre-training**
    
    - Self-supervised learning
        
    - Massive unlabeled data
        
- **Fine-tuning**
    
    - Full Fine-tuning
        
    - **Parameter-Efficient Fine-Tuning (PEFT)**
        
        - LoRA (Low-Rank Adaptation)
            
        - Adapter Tuning
            
        - Prompt Tuning / P-Tuning
            

### Alignment

- **Reinforcement Learning from Human Feedback (RLHF)**
    
    - SFT (Supervised Fine-tuning)
        
    - Reward Model
        
    - Reinforcement Learning (PPO)
        

### Inference

- **Decoding Strategies**
    
    - Greedy Search
        
    - Beam Search
        
    - Top-K Sampling
        
    - **Nucleus (Top-p) Sampling**
        
- **Inference Optimization**
    
    - **KV Cache**
        
    - **Quantization**
        
    - Speculative Decoding
        

***
## IV. Model Classification & Evolution 

- **Encoder-Only Models**
    
    - BERT, RoBERTa
        
    - Excels at: Natural Language Understanding (NLU)
        
- **Decoder-Only Models**
    
    - **GPT series**, Llama, Mistral
        
    - Excels at: Natural Language Generation (NLG)
        
- **Encoder-Decoder Models**
    
    - T5, BART
        
    - Excels at: Sequence-to-Sequence (Seq2Seq) tasks
        

***
## V. Applications & Evaluation 

### Typical Applications

- Text Generation, Summarization, Q&A, Translation
    
- Code Generation
    
- **RAG (Retrieval-Augmented Generation)**
    

### Evaluation Metrics

- **Perplexity**
    
- BLEU (for Translation)
    
- ROUGE (for Summarization)