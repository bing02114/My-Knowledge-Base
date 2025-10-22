### 1.Full Fine-tuning

#### 1.1 Concept

>This is the traditional method of fine-tuning. It involves updating **all the weights** of the pre-trained model while training it on a smaller, task-specific labeled dataset.

### 1.2 Advantages

>Often achieves the highest performance for the target task.

#### 1.3 Disadvantages

>**Computationally Expensive:** Updating billions of parameters requires significant GPU resources
>
>**High Storage Cost:** A complete, separate copy of the model must be stored for each downstream task

***

### 2.Parameter-Efficient Fine-Tuning (PEFT)

>A collection of methods designed to adapt a pre-trained model to new tasks by updating only a small fraction of its parameters, keeping the vast majority of the original model's weights frozen.

**Core Advantages**

- **Reduces Computational & Storage Costs:** Drastically lowers the GPU memory requirements and the storage space needed for fine-tuned models. 
    
- **Avoids Catastrophic Forgetting:** By keeping the original weights frozen, it helps prevent the model from "forgetting" the general knowledge learned during pre-training. 
    
- **Portability:** The small number of trained parameters (the "adapter") can be easily shared and plugged into the original base model.

#### 2.1 LoRA (Low-Rank Adaptation) 

>LoRA hypothesizes that the change in weights during fine-tuning has a low "intrinsic rank." Instead of updating the full weight matrix W, it freezes W and trains two small, low-rank matrices A and B whose product BA approximates the change ΔW. During inference, the update is added to the original weights: W′=W+BA.

#### 2.2 Adapter Tuning

>This method inserts small, new neural network modules, called "adapters," inside each layer of the pre-trained Transformer. During fine-tuning, only the weights of these newly added adapter modules are trained, while the original Transformer layers remain frozen.

#### 2.3 Prompt Tuning / P-Tuning

* These methods freeze the entire language model and focus on optimizing the input prompt instead.

**Prompt Tuning**

>Prepends a small number of continuous, learnable vectors (soft prompts) to the input sequence's embeddings. Only these prompt vectors are updated during training.

**Prompt Tuning**

>A more advanced version that gives the model more flexibility by inserting learnable prompts not just at the beginning but also at intermediate layers of the model, and it uses a small LSTM or MLP to generate these prompts.