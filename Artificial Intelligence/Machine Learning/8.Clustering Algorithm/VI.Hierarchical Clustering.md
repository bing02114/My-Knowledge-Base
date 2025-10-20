### 1.AGNES (AGglomerative NESting)

#### 1.1 Strategy

>It's a bottom-up agglomerative algorithm. It starts by treating each sample as a single cluster and then iteratively merges the two closest clusters until a specified number of clusters is reached

#### 1.2 Cluster Distance

>The distance between clusters can be calculated in several ways:

**Single-linkage**: Minimum distance between samples in the two clusters (dmin​).

**Complete-linkage**: Maximum distance between samples in the two clusters (dmax​).

**Average-linkage**: Average distance between all pairs of samples from the two clusters (davg​).

***
### 2.Properties

**Does not require specifying the number of clusters**

**Greedy nature and irreversible merges/splits**

**Can be computationally expensive**

**Provides a rich, multi-level view of the data**
