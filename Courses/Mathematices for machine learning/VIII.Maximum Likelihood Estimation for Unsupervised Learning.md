### 1.The Probabilistic View of "Label Nosie"

>The central idea is to treat the observed label y as a random variable that is a funciton of our model's prediction $\hat{y}$

* **Assumption**: We assuem the true label y is our model's "perfect" prediction plus some random noise
* **Model**: $y=\hat{y}+\epsilon$
* **Noise Model**: We assuem the noise is drawn from a Gaussian distribution with a mean of 0 and some variance
* **Resulting Probabilitstic Model**: Using the **Change of Variables** rule, this assumption is equivalent to saying that y itself is a random variable drawn from a Gaussian distribution centered at our prediciton.

### 2.Key Probability Tools

**Product Rule**

$$P(x,y)=P(x|y)P(y)$$

**Law of Total Expectation**

$$E_y[E[x|y]]=E[x]$$

**Change of Variables**

$$f_y(y)=f_x(g^{-1}(y))·|\frac{d}{dy}g^{-1}(y)|$$

**LOTUS - Law of the Unconscious Statistician**

$$E_{p(z)}[f(g(z))]=E_{p(x)}[f(x)]$$

### 3.MLE for Linear Regression

#### 3.1 State the Model

$$y\sim N(x^{T}\theta,\sigma^2)$$

#### 3.2 Write the Likelihood

$$p(y^{i}|x^{(i)T}\theta,\sigma^2)=\frac{1}{\sqrt{2\pi \sigma^2}}exp(-\frac{(y^{(i)}-x^{(i)T}\theta)^2}{2\sigma^2})$$

>Assuming all m data points are i.i.d.

$$p(D|theta)=\prod^{m}_{i=1}p(y^{i}|x^{(i)T}\theta,\sigma^2)$$

#### 3.3 Find the MLE

$$L(\theta)\rightarrow LL(\theta)\rightarrow NLL(\theta)$$

$$NLL(\theta)=\frac{m}{2}log(2\pi \sigma^2)+\frac{1}{2\sigma^2}\sum^{m}_{i=1}(y^{(i)}-x^{(i)T}\theta)^2$$

#### 3.4 The Connection

$$\arg\min_{\theta}NLL(\theta)=\arg\min_{\theta}\sum^{m}_{i=1}(y^{(i)}-x^{(i)T}\theta)^2$$

>This is the Ordinary Least Squares (OLS) loss function

#### 3.5 Conclusion

$$\theta_{MLE}=\theta_{OLS}=(X^TX)^{-1}X^{T}y$$

### 4.MLE for Logistic Regression

#### 4.1 State the Model
#### 4.2 Write the Likelihood
#### 4.3 Find the MLE
#### 4.4 The Connection

>Maximizing the likelihood (MLE) of a Bernoulli model is **equivalent to** minimizing the Binary Cross-Entropy loss.