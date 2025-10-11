### 1.Introduction

Generally, to test whether a sample conforms to a certain population distribution, it is necessary to collect observed values {X1​,X2​,…,Xn​} for testing. The $\chi^2$ goodness of fit test proposed by Karl Pearson is commonly used.

### 2.Discrete Population

#### 2.1 The theoretical population does not contain unknown parameters

**Test Statistic:**

- The test statistic is:
    
- **Formula:** $\chi^2 = \sum_{i=1}^{k} \frac{(n_i - np_i)^2}{np_i} \sim \chi^2(k-1)$

#### 2.2 The theoretical distribution contains several unknown parameters

- **Test Statistic:**
    
    - The test statistic is:
        
    - **Formula:** $\chi^2 = \sum_{i=1}^{k} \frac{(n_i - n\hat{p}_i)^2}{n\hat{p}_i} \sim \chi^2(k-1-r)$
        
    - Where r is the number of unknown parameters, $\hat{p_i}$ is the maximum likelihood estimate of $p_i$​. Generally speaking, the number of kinds of maximum likelihood estimates is the number of unknown parameters.