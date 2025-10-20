### 1.Definition

>Ensemble learning completes a learning task by constructing and combining multiple learners. This is also known as a multi-classifier system

### 2.Structure

>It first generates a set of "individual learners" and then combines them using some strategy

* **Homogeneous Ensemble**: The ensemble contains only one type of individual learner, called "base learners". The corresponding algorithm is the "base learning algorithm"
* **Heterogeneous Ensemble**: The ensemble contains different types of individual learners, called "component learners".

### 3.Core Idea

>To obtain a good ensemble, the individual learners should be "good and different" —that is, they should perform reasonably well and have diversity among them.

### 4.Theoretical Guarantee

>An analysis based on the Hoeffding inequality shows that as the number of individual classifiers in an ensemble increases, the ensemble's error rate will decrease exponentially, eventually approaching zero, provided the base learners' errors are independent.


### 5.Features of Boosting

>From a bias-variance decomposition perspective, Boosting mainly focuses on reducing bias