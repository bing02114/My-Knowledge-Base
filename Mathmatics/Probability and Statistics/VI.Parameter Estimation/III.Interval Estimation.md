### 1.Defintion

>Let the population distribution $F(x;\theta)$ contain one or more unknown parameters $\theta \in \Theta$. For a given value $\alpha$ ($0 < \alpha < 1$), if two statistics determined by the sample $X_1, \dots, X_n$, $\underline{\theta} = \underline{\theta}(X_1, \dots, X_n)$ and $\bar{\theta} = \bar{\theta}(X_1, \dots, X_n)$, satisfy:
>
>$$P_{\theta}(\underline{\theta} \le \theta \le \bar{\theta}) = 1 - \alpha, \quad \forall \theta \in \Theta$$
>then $1-\alpha$ is called the **confidence level**, and the interval $(\underline{\theta}, \bar{\theta})$ is called the **confidence interval** for $\theta$ with confidence level $1-\alpha$.

### 2.Pivotal Quantity Method

**The pivotal quantity method for the parameter to be estimated $g(\theta)$**

* Find a statistic T that is related to the parameter to be estimated, $g(\theta)$. Generally, it is a good point estimator (often constructed via maximum likelihood estimation).

* Find the distribution of a certain function of T and $g(\theta)$, $S(T, g(\theta))$. The distribution of S must not depend on $\theta$ (S is the pivotal quantity).

* For any constants a < b, the inequality $a \le S(T, g(\theta)) \le b$ must be expressible in the equivalent form $A \le g(\theta) \le B$, where A and B are related to T, a, b, but not to $\theta$.

* Find the $\alpha/2$ quantile $\omega_{\alpha/2}$ and the $(1-\alpha/2)$ quantile $\omega_{1-\alpha/2}$ of the distribution F. We have $F(\omega_{1-\alpha/2}) - F(\omega_{\alpha/2}) = 1-\alpha$. Therefore:

$$P(\omega_{1-\alpha/2} \le S(T, g(\theta)) \le \omega_{\alpha/2}) = 1-\alpha$$

### 3.Common Interval Estimation for a Normal Population using the Pivotal Quantity Method

#### 3.1 σ is known, finding the two-sided confidence interval for μ with confidence level 1-α

- **Topic:**
    
    - Given that σ is known, find the two-sided confidence interval for μ with a confidence level of 1−α.
        
- **Pivot Quantity:**
    
    - The pivot quantity is defined as:
        
    - **Formula:** $Z = \frac{\bar{X} - \mu}{\frac{\sigma}{\sqrt{n}}} \sim N(0, 1)$
        
- **Two-Sided Confidence Interval:**
    
    - Thus, the resulting two-sided confidence interval is:
        
    - **Formula:** $[\bar{X} - \frac{z_{\frac{\alpha}{2}}\sigma}{\sqrt{n}}, \bar{X} + \frac{z_{\frac{\alpha}{2}}\sigma}{\sqrt{n}}]$
        
    - Where $z_{\frac{a}{2}}$​​ is the upper α/2 quantile of the standard normal distribution function.
        
- **One-Sided Upper Confidence Limit:**
    
    - The one-sided upper confidence limit is:
        
    - **Formula:** $\bar{X} + \frac{z_{\alpha}\sigma}{\sqrt{n}}$
        
- **One-Sided Lower Confidence Limit:**
    
    - The one-sided lower confidence limit is:
        
    - **Formula:** $\bar{X} - \frac{z_{\alpha}\sigma}{\sqrt{n}}$
        
- **Length of the Confidence Interval:**
    
    - The length of the confidence interval is:
        
    - **Formula:** $\frac{2z_{\frac{\alpha}{2}}\sigma}{\sqrt{n}}$

#### 3.2 Two-Sided Confidence Interval for μ (with unknown σ)

- **Topic:**
    
    - Given that σ is unknown, find the two-sided confidence interval for μ with a confidence level of 1−α.
        
- **Pivot Quantity:**
    
    - The pivot quantity is:
        
    - **Formular:** $T = \frac{\bar{X} - \mu}{\frac{S}{\sqrt{n}}} \sim t(n-1)$
        
- **Two-Sided Confidence Interval:**
    
    - Thus, the resulting two-sided confidence interval for μ is:
        
    - **Formula:** $[\bar{X} - \frac{t_{\frac{\alpha}{2}}(n-1)S}{\sqrt{n}}, \bar{X} + \frac{t_{\frac{\alpha}{2}}(n-1)S}{\sqrt{n}}]$
        
- **One-Sided Upper Confidence Limit:**
    
    - The one-sided upper confidence limit is:
        
    - **Formula:** $\bar{X} + \frac{t_{\alpha}(n-1)S}{\sqrt{n}}$
        
- **One-Sided Lower Confidence Limit:**
    
    - The one-sided lower confidence limit is:
        
    - **Formula:** $\bar{X} - \frac{t_{\alpha}(n-1)S}{\sqrt{n}}$
        
- **Length of the Confidence Interval:**
    
    - The length of the confidence interval is:
        
    - **Formula:** $\frac{2t_{\frac{\alpha}{2}}(n-1)S}{\sqrt{n}}$
        

### **3.3 Two-Sided Confidence Interval for σ² (with unknown μ)**

- **Topic:**
    
    - Given that μ is unknown, find the two-sided confidence interval for σ² with a confidence level of 1−α.
        
- **Pivot Quantity:**
    
    - The pivot quantity is:
        
    - **Formula:** $\chi_{n-1}^2 = \frac{(n-1)S^2}{\sigma^2} = \frac{1}{\sigma^2}\sum_{i=1}^{n}(X_i - \bar{X}_n)^2 \sim \chi^2(n-1)$
        
- **Two-Sided Confidence Interval:**
    
    - Therefore, the two-sided confidence interval for σ² is:
        
    - **Formula:** $[\frac{(n-1)S^2}{\chi_{\frac{\alpha}{2}}^2(n-1)}, \frac{(n-1)S^2}{\chi_{1-\frac{\alpha}{2}}^2(n-1)}]$
        
- **One-Sided Upper Confidence Limit:**
    
    - The one-sided upper confidence limit is:
        
    - **Formula:** $\frac{(n-1)S^2}{\chi_{1-\alpha}^2(n-1)}$
        
- **One-Sided Lower Confidence Limit:**
    
    - The one-sided lower confidence limit is:
        
    - **Formula:** $\frac{(n-1)S^2}{\chi_{\alpha}^2(n-1)}$

### 4.Interval Estimation for Two Normal Populations

#### 4.1 Introduction

Let $\overline{X_n}$​ and $\overline{Y_m}$​ be the sample means of {$X_i$​} and {$Y_j$​} respectively, and let $S^2_n$​ and $S^2_{m}$​ be the sample variances respectively.

- $\bar{X}_n \sim N(\mu_1, \frac{\sigma_1^2}{n})$
    
- $\bar{Y}_m \sim N(\mu_2, \frac{\sigma_2^2}{m})$
    
- $\Rightarrow \bar{X}_n - \bar{Y}_m \sim N(\mu_1 - \mu_2, \frac{\sigma_1^2}{n} + \frac{\sigma_2^2}{m})$ 

#### 4.2 Confidence Interval for $\mu_1-\mu_2$​ (with known $\sigma_1^2, \sigma_2^2$)

- **Topic:**
    
    - Confidence interval for the difference in means μ1​−μ2​ when $\sigma_1^2, \sigma_2^2$ are known.
        
- **Pivot Quantity:**
    
    - The pivot quantity is:
        
    - **Formula:** $Z = \frac{(\bar{X}_n - \bar{Y}_m) - (\mu_1 - \mu_2)}{\sqrt{\frac{\sigma_1^2}{n} + \frac{\sigma_2^2}{m}}} \sim N(0, 1)$
        
- **Two-Sided Confidence Interval:**
    
    - The two-sided confidence interval for μ1​−μ2​ is:
        
    - **Formula:** $[(\bar{X}_n - \bar{Y}_m) - z_{\frac{\alpha}{2}}\sqrt{\frac{\sigma_1^2}{n} + \frac{\sigma_2^2}{m}}, (\bar{X}_n - \bar{Y}_m) + z_{\frac{\alpha}{2}}\sqrt{\frac{\sigma_1^2}{n} + \frac{\sigma_2^2}{m}}]$
        
- **One-Sided Upper Confidence Limit:**
    
    - The one-sided upper confidence limit is:
        
    - **Formula:** $(\bar{X}_n - \bar{Y}_m) + z_{\alpha}\sqrt{\frac{\sigma_1^2}{n} + \frac{\sigma_2^2}{m}}$
        
- **One-Sided Lower Confidence Limit:**
    
    - The one-sided lower confidence limit is:
        
    - **Formula:** $(\bar{X}_n - \bar{Y}_m) - z_{\alpha}\sqrt{\frac{\sigma_1^2}{n} + \frac{\sigma_2^2}{m}}$

#### 4.3 Confidence Interval for $μ1​−μ2$​ (with $σ12​,σ22$​ unknown, but $σ12​=σ22​=σ2$)

- **Pooled Sample Variance:**
    
    - **EN:** The pooled sample variance is:
        
    - **Formula:** $S_w^2 = \frac{(n-1)S_1^2 + (m-1)S_2^2}{n+m-2}$
        
- **Pivot Quantity:**
    
    - **EN:** Using $S_w^2$ as a substitute for $σ12​,σ22​$, the new pivot variable is:
        
    - **Formula:** $T = \frac{(\bar{X}_n - \bar{Y}_m) - (\mu_1 - \mu_2)}{S_w\sqrt{\frac{1}{n} + \frac{1}{m}}} \sim t(n+m-2)$
        
- **Two-Sided Confidence Interval:**
    
    - **EN:** The two-sided confidence interval for μ1​−μ2​ is:
        
    - **Formula:** $[(\bar{X}_n - \bar{Y}_m) - t_{\frac{\alpha}{2}}(n+m-2)S_w\sqrt{\frac{1}{n}+\frac{1}{m}}, (\bar{X}_n - \bar{Y}_m) + t_{\frac{\alpha}{2}}(n+m-2)S_w\sqrt{\frac{1}{n}+\frac{1}{m}}]$
        

#### 4.4 Confidence Interval for $μ1​−μ2$​ (with $σ12​,σ22​ $unknown, but $σ12​/σ22​=b2$ known)

- **Pooled Sample Variance:**
    
    - The pooled sample variance is:
        
    - **Formula:** $S_b^2 = \frac{(n-1)S_1^2}{b^2} + \frac{(m-1)S_2^2}{n+m-2}$
        
- **Pivot Quantity:**
    
    - Using $S_b^2$​ as a substitute for $\sigma^2_2$​, the new pivot variable is:
        
    - **Formula:** $T = \frac{(\bar{X}_n - \bar{Y}_m) - (\mu_1 - \mu_2)}{S_b\sqrt{\frac{b^2}{n} + \frac{1}{m}}} \sim t(n+m-2)$
        
- **Two-Sided Confidence Interval:**
    
    - The two-sided confidence interval for μ1​−μ2​ is:
        
    - **Formula:** $[(\bar{X}_n - \bar{Y}_m) - t_{\frac{\alpha}{2}}(n+m-2)S_b\sqrt{\frac{b^2}{n}+\frac{1}{m}}, (\bar{X}_n - \bar{Y}_m) + t_{\frac{\alpha}{2}}(n+m-2)S_b\sqrt{\frac{b^2}{n}+\frac{1}{m}}]$

#### 4.5 Confidence Interval for the Ratio of Variances $\frac{\sigma^2_2}{\sigma^2_1}$

- **Pivot Quantity:**
    
    - The pivot quantity is:
        
    - **Formula:** $F = \frac{S_1^2/S_2^2}{\sigma_1^2/\sigma_2^2} \sim F(n-1, m-1)$
        
- **Two-Sided Confidence Interval:**
    
    - The two-sided confidence interval for the ratio of variances is:
        
    - **Formula:** $[\frac{S_1^2/S_2^2}{F_{\frac{\alpha}{2}}(n-1, m-1)}, \frac{S_1^2/S_2^2}{F_{1-\frac{\alpha}{2}}(n-1, m-1)}]$
