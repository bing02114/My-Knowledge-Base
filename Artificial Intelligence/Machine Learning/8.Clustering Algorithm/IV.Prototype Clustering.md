### 1.K-means Algorithm

#### 1.1 Objective

>To partition the data into _k_ clusters such that the sum of squared errors between samples and their assigned cluster's mean vector (prototype) is minimized. This is an NP-hard problem.

$$E=\sum^{k}_{i=1}\sum_{x\in C_{i}}||x-\mu_{i}||^{2}_{2}$$
#### 1.2 Process

It uses a greedy iterative approach: 

(1) Randomly initialize _k_ mean vectors. 

(2) Assign each sample to the cluster of the nearest mean vector. 

(3) Re-calculate the mean vector for each cluster. 

(4) Repeat steps 2 and 3 until the mean vectors no longer

***
### 2.Learning Vector Quantization (LVQ)

#### 2.1 Description

This is a supervised clustering algorithm that uses class labels to guide the clustering process.

#### 2.2 Process

It finds the nearest prototype vector to a sample. If the prototype's class label matches the sample's, the prototype is moved closer to the sample; if not, it is moved away.

***
### 3.Gaussian Mixture Clustering
#### 3.1 Concept

>This method uses a probability model to represent the clusters. It assumes that the data is generated from a mixture of several Gaussian distributions, where each component corresponds to a cluster

#### 3.2 Model 

>The probability density of the mixture is pM​(x)=∑i=1k​αi​⋅p(x∣μi​,Σi​), where αi​ is the mixing coefficient

$$p_{M}(x)=\sum^{k}_{i=1}\alpha·p(x|\mu_i ,\Sigma_{i})$$

#### 3.3 Parameter Estimation

>The model parameters (αi​,μi​,Σi​) are typically estimated using the **Expectation-Maximization (EM) algorithm**

***
### 4.Properties

**The number of clusters _k_ must be specified beforehand**

**Sensitive to the initialization of prototypes**

**Often limited to specific cluster shapes**

**Model assumptions must be accurate for generative models**