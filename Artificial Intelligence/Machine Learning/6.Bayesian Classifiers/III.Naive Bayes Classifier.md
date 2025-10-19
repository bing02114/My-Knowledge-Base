### 1.Core Idea

>To overcome the difficulty of estimating the joint class-conditional probability P(x∣c), the Naïve Bayes classifier adopts the "attribute conditional independence assumption". This assumes all attributes are independent of each other given the class

### 2.Classification Rule

$$h_{nb}(x)=\arg\max_{c\in y}P(c)\prod^{d}_{i=1}P(x_{i}|c)$$
p