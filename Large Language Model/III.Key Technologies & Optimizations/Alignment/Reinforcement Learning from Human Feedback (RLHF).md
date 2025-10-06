### I.Definition

>Reinforcement Learning from Human Feedback (RLHF) is a technique used to align a language model's behavior with human preferences and values. The goal is to make the model more helpful, honest, and harmless beyond what can be achieved with standard supervised training alone.


### II.SFT (Supervised Fine-tuning)

>**Goal:** To teach the base model the desired response format and style.
>
>A pre-trained language model is fine-tuned on a high-quality, curated dataset of "prompt-response" pairs created by human labelers. This adapts the model to the target domain (e.g., a helpful assistant).


### III.Reward Model

>**Goal:** To create a model that can automatically score responses based on human preferences.
>
>The SFT model generates several answers to a single prompt. A human labeler then ranks these answers from best to worst. This ranking data is used to train a separate model—the Reward Model—which learns to predict which responses humans would prefer.

### IV.Reinforcement Learning (PPO)

>**Goal:** To use the Reward Model to improve the language model's policy.
>
>The SFT model is further fine-tuned using a reinforcement learning algorithm (commonly PPO - Proximal Policy Optimization). The model's "action" is to generate a response to a prompt. The "reward" is the score given by the Reward Model. The RL algorithm updates the language model's weights to encourage it to generate responses that maximize this reward score.

### V.Importance

>**Alignment with Human Values:** RLHF is the primary method for "aligning" AI. It steers the model away from generating undesirable outputs (e.g., toxic, biased, or false information) and towards outputs that are helpful, harmless, and honest.
>
>**Handling Nuance:** It allows the model to learn nuanced and complex human preferences that are difficult to specify with a simple loss function. For example, it can learn the difference between a technically correct answer and a truly helpful one.
>
>**Improving Safety:** By training the model to avoid responses that humans rank poorly due to safety concerns, RLHF is a critical tool for building safer and more reliable AI systems.

### VI.Reward Hacking / **Over-optimization**

>**Reward Hacking** is a phenomenon in artificial intelligence, particularly in reinforcement learning, where an AI agent finds an unexpected and undesirable way to maximize its reward, which does not align with the human designer's original intent.
>
>behaviours: <font color="red">Value Misalignment、Fabricating Answers / Hallucination、Verboseness</font>

