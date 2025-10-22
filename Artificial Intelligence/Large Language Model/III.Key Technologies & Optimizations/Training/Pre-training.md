### 1.Core Idea

>To learn general-purpose knowledge and representations about a domain (e.g., language, vision) by training on an enormous dataset without human-provided labels.

### 2.Learning Method: Self-supervised learning

>This is a type of machine learning where the training data provides the supervision signal itself. The model is given a pretext task where the objective (the "label") can be automatically generated from the input data.

>**Examples:** For language models, this includes Masked Language Modeling (predicting masked words) and Causal Language Modeling (predicting the next word). The "labels" are simply the parts of the text that were hidden from the model.

### 3.Data: Massive unlabeled data

>Pre-training leverages vast quantities of readily available, unlabeled data, such as the text from the entire internet (e.g., Common Crawl), all of Wikipedia, or large book corpora. This is a key advantage as it doesn't require expensive and time-consuming manual annotation.

