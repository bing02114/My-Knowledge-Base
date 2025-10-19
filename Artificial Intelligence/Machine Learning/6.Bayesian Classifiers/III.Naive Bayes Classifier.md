### 1.Core Idea

>To overcome the difficulty of estimating the joint class-conditional probability P(x∣c), the Naïve Bayes classifier adopts the "attribute conditional independence assumption". This assumes all attributes are independent of each other given the class

### 2.Classification Rule

$$h_{nb}(x)=\arg\max_{c\in y}P(c)\prod^{d}_{i=1}P(x_{i}|c)$$

### 3.Laplacian Correctino

To prevent a conditional probability from becoming zero due to an attribute value not appearing with a class in the training set, "smoothing" is performed, commonly using Laplacian correction.


$$P(c)=\frac{1+|D_c|}{N+|D|}$$

where
* N: number of different kinds of evidence

### 4.Main Types of Naive Bayes Classifiers

#### 4.1 Gaussian Naive Bayes

**When to Use**

>This classifier is used when your features are **continuous numerical values** that can be assumed to follow a Gaussian (or Normal) distribution, i.e., a bell curve

**Core Assumption**

>For a given class, the values of each feature are normally distributed. The algorithm doesn't need to see the exact probability of a specific value (which is zero for continuous data), but rather how well that value fits into the bell curve defined by the data of that class.

**Likelihood**

$$P(x_{i}|Class_{k})=\frac{1}{\sqrt{2\pi\sigma^{2}_{k}}}exp(-\frac{(x_{i}-\mu_{k})^{2}}{2\sigma^{2}_{k}})$$

#### 4.2 Multinomial Naive Bayes

**When to Use**

>This is the classic choice for features that represent **discrete counts**. Its most famous application is in text classification.

**Core Assumption**

>The features are assumed to be generated from a multinomial distribution, which is a generalization of the binomial distribution. For text, this means we are modeling the probability of seeing a certain word, given the class

**Likelihood**

$$P(word_{i}|Class_{k})=\frac{N_{ki}+\alpha}{N_{k}+\alpha·V}$$
>V: The total number of unique words in the vocabulary

#### 4.3 Bernoulli Naive Bayes

**When to Use**

>This classifier is used for features that are **binary (0 or 1)**, representing the **presence or absence** of a feature

**Core Assumption**

>The features are independent binary variables generated from a Bernoulli distribution. The key difference from Multinomial NB is that BNB doesn't care about _how many times_ a word appears, only _if_ it appears

**Likelihood**

$$P(feature_{i}~is~present |Class_{k})=\frac{N_{ki}+\alpha}{N_{k}+2\alpha}$$