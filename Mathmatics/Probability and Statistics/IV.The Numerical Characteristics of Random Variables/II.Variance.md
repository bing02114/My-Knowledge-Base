### 1.Definition)

- **1.Basic**
    
    - The variance is defined as the expectation of the squared deviation of a random variable from its mean. It has a useful computational formula:
	    
      $D(X) = E[(X-\mu)^2] = E(X^2) - \mu^2 = E(X^2) - (E(X))^2$
        
- **2.Discrete Case**
    
    - $D(X) = \sum_{i=1}^{+\infty} [x_i - E(X)]^2 p_i$
        
- **3.Continuous Case**
    
    - $D(X) = \int_{-\infty}^{+\infty} [x - E(X)]^2 f(x) dx$
        

#### **2.Properties**

1. $0 \le Var(X) = E(X^2) - (E(X))^2 \Rightarrow Var(X) \le E(X^2)$
    
2. $Var(cX) = c^2 Var(X)$
    
3. $Var(X) \le E[(X-c)^2]$, where equality holds if and only if $c = E(X)$
    
4. $Var(X+Y) = Var(X) + Var(Y) + 2 \cdot Cov(X,Y)$
    
5. $Var(X-Y) = Var(X) + Var(Y) - 2 \cdot Cov(X,Y)$
    
6. If X,Y are mutually independent and a,b are constants, then $Var(aX + bY) = a^2 Var(X) + b^2 Var(Y)$
    
7. The variance of the sample mean $\bar{X}$ is $Var(\bar{X}) = \frac{\sigma^2}{n}$
    
8. For independent random variables X,Y, the variance of their product is $Var(XY) = Var(X)Var(Y) + Var(X)(E(Y))^2 + Var(Y)(E(X))^2$
    

#### **3.Standardization**

- We call the following the standardized random variable of X:
    
- $X^* = \frac{X - E(X)}{\sqrt{Var(X)}}$
    
- for X as the standardized random variable. It is easy to show that $E(X^*) = 0, Var(X^*) = 1$.

