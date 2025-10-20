### 1.Mechanism

>k-Nearest Neighbor (kNN) is a supervised learning method. Given a test sample, it finds the _k_ training samples in the training set that are closest to it based on some distance metric. Predictions are then made based on the information from these _k_ "neighbors."

**Classification**: Uses "voting," selecting the class label that appears most frequently among the _k_ neighbors.

**Regression**: Uses "averaging," taking the mean of the real-valued output labels of the _k_ neighbors as the prediction.

### 2.Lazy Learning

>kNN is a prominent example of "lazy learning." It does not have an explicit training process; instead, it simply stores the training samples. The computation is deferred until a test sample is received. In contrast, methods that process samples during the training phase are called "eager learning."

### 3.Error Bound

>The generalization error rate of a 1-NN classifier is no more than twice the error rate of the Bayes optimal classifier.