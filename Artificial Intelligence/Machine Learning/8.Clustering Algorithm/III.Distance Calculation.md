### 1.Minkowski Distance

* $dist_{mk}(x_i,x_j)=(\sum^{n}_{u=1}|x_{iu}-x_{ju}|^{p})^{1/p}$
* **Euclidean Distance**: When p=2
* **Manhattan Distance**: When p=1

### 2.Value Difference Metric

>For "non-ordinal attributes"

$$VDM_p (a,b)=\sum^{k}_{i=1}|\frac{m_{u,a,i}}{m_{u,a}}-\frac{m_{i,b,i}}{m_{u,b}}|^{p}$$

### 3.Weighted Distance

Attributes can be assigned different weights to reflect their importance

$$dist_{wmk}(x_i,x_j)=(w_1 |x_{i1}-x_{j1}|^{p}+\dots+w_n |x_{in}-x_{jn}|^{P})^{1/p}$$

