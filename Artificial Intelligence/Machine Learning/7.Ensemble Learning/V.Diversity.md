### 1.Error-Ambiguity Decomposition

* For regression tasks, the generalization error of an ensemble can be decomposed as: E=Eˉ−Aˉ
* Eˉ is the weighted average of the individual learners' generalization errors, and Aˉ is the weighted "ambiguity" (or diversity) of the individual learners
* **Implication**: This shows that the better and more diverse the individual learners are, the better the ensemble will be

### 2.Diversity Enhancement Strategies

>Common approaches involve introducing randomness into the learning process

**Data Sample Perturbation**: Generate different data subsets via sampling, such as bootstrap sampling in Bagging. This is highly effective for "unstable" base learners (e.g., decision trees, neural networks)

**Input Attribute Perturbation**: Train base learners on different subsets of attributes (subspaces), such as in the Random Subspace algorithm

**Output Representation Perturbation**: Manipulate the output representations, such as by flipping class labels or transforming classification outputs into regression outputs.

**Algorithm Parameter Perturbation**: Use different parameter settings for the base learning algorithm to generate diverse individual learners