### 1.Core Idea of GBDT

>Gradient Boosting Decision Tree (GBDT) is a powerful machine learning technique that belongs to the boosting family of ensemble methods. 
>
>Unlike AdaBoost, which focuses on the errors of previous learners by adjusting sample weights, GBDT builds the model in a stage-wise fashion. 
>
>Each new tree (weak learner) is trained to correct the errors of the previous ones. 
>
>Specifically, each new tree is trained to predict the **negative gradient** of the loss function with respect to the predictions of the existing ensemble. 
>
>This approach allows GBDT to optimize arbitrary differentiable loss functions, making it highly flexible and applicable to both regression and classification tasks.

### 2.The GBDT Algorithm Steps

>Let's consider a regression problem with a training dataset D={(x1​,y1​),(x2​,y2​),...,(xN​,yN​)}, where xi​ is the feature vector and yi​ is the continuous target value. We will use the Mean Squared Error (MSE) as our loss function for simplicity.

$$L(y,F(x))=\frac{1}{2}(y-F(x))^{2}$$

**Step1: Initialize the model**

>The model starts with an initial constant value prediction, which is the value that minimizes the loss function over the entire dataset. For the MSE loss function, this is simply the mean of all target values yi​.

$$F_{0}(x)=\arg\min_{\gamma}\sum^{N}_{i=1}L(y_{i},\gamma)=\arg\min_{\gamma}\sum^{N}_{i=1}\frac{1}{2}(y_{i}-\gamma)^{2}=\overline{y}$$

**Step2: Iterate for M weak learners (m=1 to M)**

**a) Calculate the negative gradient (pseudo-residuals)**

>For each sample, calculate the negative gradient of the loss function with respect to the previous prediction Fm−1​(xi​). For MSE, this gradient is simply the residual (the difference between the true value and the predicted value). This is why GBDT can be seen as fitting the residuals.

$$r_{im}=-[\frac{\partial L(y_{i},F(x_{i}))}{\partial F(x_{i})}]_{F(x)=F_{m-1}(x)}$$

$$r_{im}=y_{i}-F_{m-1}(x_{i})$$

**b) Fit a new weak learner to the pseudo-residuals**

>Train a new regression tree (the weak learner), hm​(x), using the pseudo-residuals rim​ as the target values. The dataset for this step is {(x1​,r1m​),(x2​,r2m​),...,(xN​,rNm​)}. This tree learns the error patterns of the previous ensemble. Let the terminal regions (leaves) of this tree be Rjm​ for j=1,2,...,Jm​.

**c) Find the best output value for each leaf**

>For each leaf j of the new tree hm​(x), find the optimal output value γjm​ that minimizes the loss function for all samples in that leaf. This value is a single prediction for all samples that fall into that leaf.

$$\gamma_{jm}=\arg\min_{\gamma}\sum_{x_{i}\in R_{jm}}L(y_{i},F_{m-1}(x_{i})+\gamma)$$

**d) Update the model**

>Update the ensemble model by adding the new tree, scaled by a learning rate η (eta). The learning rate (also known as shrinkage) is used to reduce the contribution of each tree, which helps prevent overfitting.

$$F_{m}(x)=F_{m-1}(x)+η\sum^{J_m}_{j=1}\gamma_{jm}I(x\in R_{jm})$$


**Step3: Output the final model**

>After M iterations, the final prediction is given by the ensemble model FM​(x).

$$G(x)=F_{M}(x)=F_{0}(x)+\sum^{M}_{m=1}η\sum^{J_{m}}_{j=1}\gamma_{jm}I(x\in R_{jm})$$


### 3.GBDT for Classification

For classification, the principle is the same, but the loss function changes. For binary classification, the **Log-Loss** (or Binomial Deviance) is commonly used.

1. **Initialize:** The initial prediction F0​(x) is the log of the odds of the positive class.
    
2. **Calculate Pseudo-Residuals:** The pseudo-residuals are calculated as the negative gradient of the Log-Loss function. They are yi​−pi​, where pi​ is the probability predicted by the model for class 1.
    
3. **Update:** The process of fitting trees and updating the model continues as in the regression case. The final output FM​(x) is in the log-odds space and needs to be converted to a probability using the sigmoid function: P(y=1∣x)=1+e−FM​(x)1​.

### 4.Summary of GBDT's Characteristics

- **High Predictive Power:** GBDT is one of the most powerful "off-the-shelf" algorithms and is known for its high accuracy.
    
- **Flexibility:** It can optimize any differentiable loss function, making it suitable for regression, classification, and ranking problems.
    
- **Handles Mixed Data Types:** Like decision trees, it can naturally handle numerical and categorical features.
    
- **Prone to Overfitting:** It can easily overfit if the number of trees (M) is too large. This can be mitigated by using a learning rate (η), subsampling, and limiting tree depth.
    
- **Computationally Expensive:** Training can be slow because the trees are built sequentially; the training of tree m depends on the result of tree m−1.