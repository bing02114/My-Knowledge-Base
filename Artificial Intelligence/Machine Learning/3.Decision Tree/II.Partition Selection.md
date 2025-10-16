### 1.Information Gain (ID3)

#### 1.1 Information Entropy

>A common measure of the purity of a sample set D. The lower its value, the higher the purity.

$$Ent(D)=-\sum^{|\gamma|}_{k=1}p_{k}log_{2}p_{k}$$
where $p_{k}$ is the proportion of samples in class k

#### 1.2 Information Gain

>Measures the "purity improvement" gained by splitting dataset D with an attribute _a_. A larger gain means a greater purity improvement. The ID3 algorithm uses information gain as its criterion.

$$Gain(D,a)=Ent(D)-\sum^{V}_{v=1}\frac{|D^{v}|}{|D|}Ent(D^{v})$$
**Drawback:**

> Information gain is biased towards **attributes with a larger number of possible values**

***
### 2.Gain Ratio (C4.5)

#### 2.1 Definition

>The C4.5 algorithm uses gain ratio instead of information gain to reduce the bias

$$Gain\_ratio(D,a)=\frac{Gain(D,a)}{IV(a)}$$

where

$$IV(a)=-\sum^{V}_{v=1}\frac{|D^{v}|}{|D|}log_{2}\frac{|D^{v}|}{|D|}$$
#### 2.2 Heuristic

>The C4.5 algorithm doesn't directly choose the attribute with the maximum gain ratio. Instead, it first finds attributes with information gain above the average, and then selects the one with the highest gain ratio from this subset.

***
### 3.Gini Index (CART)

#### 3.1 Definition

>The CART decision tree uses the Gini index to select the splitting attribute. The Gini index measures the impurity of a dataset D

$$Gini(D)=1-\sum^{|\gamma|}_{k=1}p^{2}_{k}$$

#### 3.2 Attribute Gini Index

>The goal is to choose the attribute that minimizes the Gini index after the split.

$$Gini\_index(D,a)=\sum^{V}_{v=1}\frac{|D^{v}|}{|D|}Gini(D^{v})$$

