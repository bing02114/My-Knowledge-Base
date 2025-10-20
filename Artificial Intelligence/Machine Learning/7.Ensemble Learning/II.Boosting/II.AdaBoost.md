### 1.Core Idea

>AdaBoost, short for Adaptive Boosting, is a powerful ensemble learning algorithm. 
>
>The core idea is to combine multiple "weak" learners (classifiers that are only slightly better than random guessing) into a single "strong" learner (a classifier with high accuracy). 
>
>It achieves this by training a sequence of weak learners, where each subsequent learner pays more attention to the data points that were misclassified by its predecessors. 
>
>This is done by adaptively adjusting the weights of the training samples. 
>
>Samples that are hard to classify get higher weights, forcing the next learner to focus on them.

### 2.The AdaBoost Algorithm Steps

* Let's consider a binary classification problem with a training dataset D={(x1​,y1​),(x2​,y2​),...,(xN​,yN​)}, where xi​ is the feature vector of the i-th sample and yi​∈{−1,+1} is its class label.

**Step1: Initialize the weights of the training samples**

$$w_{i}^{(m)}=\frac{1}{N}~for~i=1,2,\dots,N$$


**Step2: Iterative for M weak learns (m=1 to M)**

For each iteration m:

**a) Train a weak learner**

>Train a weak classifier Gm​(x) on the training data using the sample weights w(m). The goal of the weak learner is to find a decision rule that minimizes the weighted classification error.

**b) Calculate the weighted error rate of the learner**

>Calculate the sum of weights of the misclassified samples. This is the weighted error rate ϵm​ for the classifier Gm​(x).

$$\epsilon_{m}=\sum^{N}_{i=1}w_{i}^{m}I(G_{m}(x_{i})\neq y_{i})$$

where $I()$ is the indicator function (it is 1 if the condition is true, and 0 otherwise)

**c) Calculate the weight of the weak learner**

>Calculate a weight, αm​, for the weak learner Gm​(x) based on its error rate. More accurate classifiers are given higher weights. A classifier with an error of 0.5 (random guessing) gets a weight of 0.

$$\alpha_{m}=\frac{1}{2}ln(\frac{1-\epsilon_{m}}{\epsilon_{m}})$$

**d) Update the weights of the training samples**

>Increase the weights of the samples that were misclassified by Gm​(x) and decrease the weights of the correctly classified ones. This ensures the next learner, Gm+1​(x), will focus more on the "hard" examples.

$$w_{i}^{m+1}=\frac{w_{i}^{m}}{Z_{m}}exp(-\alpha_{m}y_{i}G_{m}(x_i))$$

$$Z_m=\sum^{N}_{i=1}w_{i}^{(m)}exp(-\alpha_{m}y_{i}G_{m}(x_i))$$

**Step3: Combine the weak learners**

>The final strong classifier, G(x), is formed by a weighted majority vote of all the weak learners. The weight of each learner's vote is its calculated αm​.

$$G(x)=sign(\sum^{M}_{m=1}\alpha_{m}G_{m}(x))$$

### 3.Summary of AdaBoost's Characteristics 

- **High Accuracy:** It can achieve high classification accuracy, often better than individual weak learners.
    
- **Flexibility:** It can be used with any classification algorithm as the base (weak) learner. Decision stumps (one-level decision trees) are a popular choice.
    
- **Sensitivity to Noisy Data and Outliers:** Because AdaBoost focuses on hard-to-classify examples, it can be sensitive to noisy data and outliers, as it might overfit by trying too hard to classify them correctly.
    
- **Relatively Simple to Implement:** The core logic is straightforward to implement.