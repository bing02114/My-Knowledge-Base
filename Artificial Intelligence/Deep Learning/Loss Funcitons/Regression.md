### 1.Mean Absolute Error (MAE) / L1

>The average of the absolute differences between the predicted values and the actual values.

$$\text{MAE} = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)$$

**Properties**

>It is robust to outliers. Because it does not square the errors, large errors are not penalized as heavily as in MSE.

**Derivative**

$$\frac{1}{n}sign(\hat{y_{i}}-y_{i})$$


### 2.Mean Squared Error (MSE) / L2

>The average of the squared differences between the predicted values and the actual values.

$$MSE=\frac{1}{n}\sum^{n}_{i=1}(y_{i}-\hat{y_{i}})^2$$

**Properties**

>**It penalizes large errors more heavily than small errors due to the squaring. It is differentiable, which makes it easy to use with gradient-based optimization methods. However, it is sensitive to outliers.**

**Derivative**

$$\frac{2}{n}(\hat{y_{i}}-y_{i})$$


### 3.Huber Loss

>A combination of MSE and MAE. It is quadratic for small errors and linear for large errors.

$$L_{\delta}(y, \hat{y}) = \begin{cases} \frac{1}{2}(y - \hat{y})^2 & \text{for } |y - \hat{y}| \le \delta \\ \delta(|y - \hat{y}| - \frac{1}{2}\delta) & \text{otherwise} \end{cases}$$

**Properties**

>It combines the best of both worlds: it is less sensitive to outliers than MSE (like MAE) and is differentiable at 0 (unlike MAE). The hyperparameter δ defines the threshold at which the function switches from quadratic to linear.


