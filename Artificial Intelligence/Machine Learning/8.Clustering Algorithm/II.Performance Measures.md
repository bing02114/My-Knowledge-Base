### 1.External Indices

>These compare the clustering result with a "reference model" (e.g., ground-truth labels). This involves creating pairs of samples and categorizing them into four sets based on whether they are in the same or different clusters in both the algorithm's result (C) and the reference model (C*).
![](../8.Clustering%20Algorithm/images/abcd.png)

#### 1.1 Jaccard Coefficient (JC)

$$JC=\frac{a}{a+b+c}$$

#### 1.2 Fowlkes and Mallows Index (FMI)

$$FMI=\sqrt{\frac{a}{a+b}·\frac{a}{a+c}}$$

#### 1.3 Rand Index (RI)

$$RI=\frac{2(a+d)}{m(m-1)}$$

>The value is in the interval [0,1], and the higher the value, the better the performace

### 2.Internal Indices

>These evaluate the clustering result directly without any external reference.

#### 2.1 Davies-Bouldin Index - DBI

$$DBI=\frac{1}{k}\sum^{k}_{i=1}max_{j\neq }i(\frac{avg(C_{i})+avg(C_{j})}{d_{cen}(\mu_{i},\mu_{j})})$$

>A smaller value is better

#### 2.2 Dunn Index - DI

$$DI=min_{\1leq i\leq k}]\{min_{j\neq i}(\frac{d_{min}(C_{i},C_{j})}{max_{1\neq l\neq k}diam(C_{l})})\}$$

>A larger value is better