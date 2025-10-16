### 1.Decomposition Strategy

>The basic idea is to decompose a multi-class task into several binary classification tasks

### 2.Classic Strategies

* **One vs. One (OvO)**: Pairs up _N_ classes, creating _N_(_N_-1)/2 binary classifiers. 
* **One vs. Rest (OvR)**: Trains _N_ classifiers, each treating one class as positive and all other classes as negative
* **Many vs. Many**: Each time, several classes are treated as positive, and several others as negative. A common MvM technique is "Error-Correcting Output Codes" (ECOC)
