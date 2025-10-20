### 1.Machanism

>It is a leading example of parallel ensemble learning methods. 
>
>It uses bootstrap sampling to generate multiple different training subsets from the initial dataset. 
>
>A base learner is then trained on each subset, and these learners are combined. 

### 2.Combining Strategy

>For classification, it typically uses simple voting; for regression, it uses simple averaging

### 3.Out-of-Bag Estimate

>Since each base learner uses only about 63.2% of the initial training samples, the remaining ~36.8% can be used as a validation set for an "out-of-bag estimate" of the generalization performance

### 4.Focus

>From a bias-variance perspective, Bagging mainly focuses on reducing variance.