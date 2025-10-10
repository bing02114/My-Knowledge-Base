### 1.Definition

**Discrete Case**

$E(X) = \sum_{k=1}^{\infty} x_k \cdot p_k$

**Continuous Case**

$E(X) = \sum_{k=1}^{\infty} x_k \cdot p_k$

### 2.Y=g(X)

**Discrete Case**

$E(Y) = E[g(X)] = \sum_{k=1}^{\infty} g(x_k) \cdot p_k$

**Continuous Case**

$E(Y) = E[g(X)] = \int_{-\infty}^{\infty} g(x) f(x) dx$

### 3.Z=h(X,Y)

**Discrete Case**

$E(Z) = E[h(X,Y)] = \sum_{i=1}^{\infty} \sum_{j=1}^{\infty} h(x_i, y_j) \cdot p_{ij}$

**Continuous Case**

$E(Z) = E[h(X,Y)] = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} h(x,y) f(x,y) dxdy$

### 4.Properties

* If the expectation of $Y = c_0 + c_1 X_1 + c_2 X_2 + \dots + c_n X_n$ exists, then: $E(c_0 + c_1 X_1 + c_2 X_2 + \dots + c_n X_n) = c_0 + c_1 E(X_1) + c_2 E(X_2) + \dots + c_n E(X_n)$

* If $X_1, X_2, \dots, X_n$ are mutually independent, and the expectation of their product $Z = X_1 X_2 \dots X_n$ exists, then $E(X_1 X_2 \dots X_n) = E(X_1) E(X_2) \dots E(X_n)$

* $E(\overline{X}) = \mu$
