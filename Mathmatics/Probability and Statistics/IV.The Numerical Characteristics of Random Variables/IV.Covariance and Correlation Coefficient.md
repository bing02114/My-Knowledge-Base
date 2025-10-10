### 1.Definition

$$Cov(X,Y) = E\{[X-E(X)][Y-E(Y)]\}$$is called the covariance of X and Y, where `Cov` is the abbreviation for the English word Covariance.

### 2.Properties

- $Cov(X,Y) = Cov(Y,X)$
    
- $Cov(X,X) = Var(X)$
    
- $Cov(X,Y) = E(XY) - E(X)E(Y)$. Thus, when X and Y are mutually independent, their covariance is 0. 
    
- $Cov(X_1+X_2, Y) = Cov(X_1, Y) + Cov(X_2, Y)$
    
- $Cov(aX, bY) = ab \cdot Cov(X,Y)$

### 3.Correlation Coefficient Definition

Let X,Y be random variables. The the following is called the correlation coefficient of X,Y:

$$\rho_{XY} = \frac{Cov(X,Y)}{\sqrt{Var(X)Var(Y)}}$$

### 4.Correlation Coefficient Properties

- When $\rho_{XY}=0$, X and Y are said to be uncorrelated (not linearly correlated)
    
- $\rho_{XY} = Cov(X^*, Y^*)$, therefore the correlation coefficient can be viewed as the covariance under a standardized scale.
	
- $|\rho_{XY}| \le 1$. The equality holds if and only if there is a strict linear relationship between X and Y. 
    
    - $\rho_{XY} = 1$, there exist $a>0, b \in \mathbb{R}$ such that $Y=aX+b$ (positive correlation). 
        
    - $\rho_{XY} = -1$, there exist $a<0, b \in \mathbb{R}$ such that $Y=aX+b$ (negative correlation). 


### 5.Uncorrelated and Independent

**Uncorrelated:** $\rho_{XY} = 0$

**Independent:** $P(X=x_i, Y=y_j) = P(X=x_i)P(Y=y_j)$, $f(x,y)=f_X(x)f_Y(y)$

>For random variables X, Y, if X and Y are **mutually independent**, then **they must be uncorrelated**. 
>
>However, if they are **uncorrelated**, they are **not necessarily independent.**

