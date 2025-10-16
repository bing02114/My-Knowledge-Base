### 1.Definition

>This refers to situations in classification tasks where the number of training examples for different classes varies greatly

### 2.Basic Strategies

>A fundamental strategy for class-imbalance learning is "rescaling" or "rebalancing". The decision rule is adjusted based on the observed odds of classes in the training set.

### 3.Common Techniques

* **Undersampling**: Removing some samples from the majority class to make the class distribution more balanced.
* **Oversampling**: Adding more samples to the minority class
* **Threshold-moving**: Directly learning on the original training set but embedding the rescaling logic into the decision-making process of the trained classifier.