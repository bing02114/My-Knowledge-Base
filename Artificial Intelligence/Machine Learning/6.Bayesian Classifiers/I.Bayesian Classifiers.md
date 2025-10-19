### 1.Bayesian Decision Theory

#### 1.1 Core Idea

>Bayesian decision theory is a fundamental method for decision-making under a probabilistic framework. For a classification task, it considers how to select the optimal class label based on probabilities and misclassification costs

#### 1.2 Conditional Risk

>The expected loss of classifying a sample x into class $C_{i}$ is called conditional risk

$$R(C_{i}|x)=\sum^{N}_{j=1}\lambda_{ij}P(C_{j}|x)$$
where $\lambda_{ij}$ is the loss of misclassifying a sample from class Cj as class Ci

#### 1.3 Bayes Decision Rule & Optimal Classifieer

>To minimize the overall risk, one only needs to choose the class label that minimizes the conditional risk for each sample. The resulting classifier is called the Bayes optimal classifier

#### 1.4 Minimizing Error Rate

>If the goal is to minimize the classification error rate, the Bayes optimal classifier simplifies to choosing the class with the highest posterior

$$h^{*}(x)=\arg\max_{c\in y}P(c|x)$$
#### 1.5 Posterior Probability Estimation Strategies

>The key challenge is to obtain the posterior probability P(c|x)

**Discriminative Models**

>Directly model P(c|x). Examples include Decision Trees, BP Neural Networks, and Support Vector Machines.

**Generative Models**

>First model the joint probability distribution P(x,c), and then derive P(c∣x) from it.

#### 1.6 Bayes' Theorem

>For generative models, P(c|x) is calculated using Bayes' theorem

$$P(c|x)=\frac{P(c)P(x|c)}{P(x)}$$

where

* P(c) is the class **prior probability**
* P(x|c) is the class-conditional probability or **likelihood**
* P(x) is the **evidence** factor for normalization