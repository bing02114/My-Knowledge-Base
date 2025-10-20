These algorithms assume that cluster structures can be identified based on the density of the sample distribution.

### 1.DBSCAN (Density-Based Spatial Clustering of Application with Noise)

#### 1.1 Core Idea

>It describes the tightness of a sample distribution based on a set of neighborhood parameters (ϵ,MinPts).

#### 1.2 Key Concepts

**ϵ-neighborhood**: The set of samples within a distance ϵ of a sample xj​.

**Core Object**: A sample with at least MinPts samples in its ϵ-neighborhood.

**Density-Reachable**: A sample xj​ is density-reachable from xi​ if there is a path of directly density-reachable samples from xi​ to xj

**Density-Connected**: Two samples are density-connected if there is a core object from which both are density-reachable
​
#### 1.3 Cluster Definition

>A cluster is defined as a maximal set of density-connected samples. DBSCAN finds clusters by starting with an arbitrary core object and expanding it by finding all density-reachable samples


***
### 2.Properties

**Can find arbitrarily shaped clusters**

**Performance is sensitive to parameters**

**Struggles with clusters of varying densities**

**Does not require specifying the number of clusters**

**Can identify noise/outliers ! ! !**

