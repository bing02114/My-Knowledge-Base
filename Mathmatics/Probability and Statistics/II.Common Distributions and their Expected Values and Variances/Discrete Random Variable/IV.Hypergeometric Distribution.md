### 1.Definition

$$X \sim H(N, M, n)$$

>The Hypergeometri distibution describes the number of successes in a sample of size n, drawn without replacement from a finite populaiton of size N that contains exactly M successes

### 2.PMF

$$P(X=k) = \frac{C_M^k C_{N-M}^{n-k}}{C_N^n}$$

### 3.Expectation

$$E(X) = n\frac{M}{N}$$

### 4.Variance

$$D(X) = n \frac{M(N-M)(N-n)}{N^2(N-1)}$$

### 5.Properties

>* **The key difference from the Binomial distribution is the dependency between trails**
>
>* When the population size N is very large compared to the sample size n, this distribution can be approximated by the Binomial distribution with p = M/N



