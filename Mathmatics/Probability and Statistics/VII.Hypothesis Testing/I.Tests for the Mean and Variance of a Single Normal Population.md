### 1.Test for the mean when the variance is known

#### 1.1 Two-sided Test

**Hypotheses**

$H_0: \mu = \mu_0 \leftrightarrow H_1: \mu \neq \mu_0$

**Test Statistic**

$U = \frac{\bar{X}_n - \mu_0}{\sigma/\sqrt{n}} \sim N(0,1)$

**Rejection Region**

Since the required significance level is α, i.e., $P_{H_0}​​(∣U∣>τ)=α$, the rejection region for the test is:

$\{|U| > u_{\frac{\alpha}{2}}\}$

That is, reject $H_0$​ when the observed value satisfies the inequality:

$\frac{\sqrt{n}|\bar{x} - \mu_0|}{\sigma} > u_{\frac{\alpha}{2}}$

reject $H_0$

#### 1.2 One-sided Test

**Right-Tailed Test**

The hypotheses are:

$H_0: \mu = \mu_0 \leftrightarrow H_1: \mu > \mu_0$` or `$H_0: \mu \le \mu_0 \leftrightarrow H_1: \mu > \mu_0$

Still using the test statistic:

$U = \frac{\bar{X}_n - \mu_0}{\sigma/\sqrt{n}}$

The rejection region is:

$\{U > u_{\alpha}\}$

**Left-Tailed Test**

Similarly, the other one-sided test is:

$H_0: \mu = \mu_0 \leftrightarrow H_1: \mu < \mu_0$` or `$H_0: \mu \ge \mu_0 \leftrightarrow H_1: \mu < \mu_0$

Then the rejection region is:

$\{U < -u_{\alpha}\}$

***

### 1.2 Test for the mean when the variance is unknown

**Two-sided Test**

- **Hypotheses:**
    
    - Consider the hypotheses:
        
    - **Formula:** $H_0: \mu = \mu_0 \leftrightarrow H_1: \mu \neq \mu_0$
        
- **Test Statistic:**
    
    - Since the variance is unknown, the sample variance can be used to substitute the population variance in the standardization process, yielding the test statistic:
        
    - **Formula:** $T = \frac{\bar{X}_n - \mu_0}{S/\sqrt{n}} \sim t(n-1)$
        
- **Rejection Region:**
    
    - The rejection region is:
        
    - **Formula:** $\{|T| > t_{\frac{\alpha}{2}}(n-1)\}$

**One-sided Test**

- **Right-Tailed Test:**
    
    - The hypotheses are:
        
    - **Formula:** $H_0: \mu = \mu_0 \leftrightarrow H_1: \mu > \mu_0$` or `$H_0: \mu \le \mu_0 \leftrightarrow H_1: \mu > \mu_0$
        
    - Still using the test statistic:
        
    - **Formula:** $T = \frac{\bar{X}_n - \mu_0}{S/\sqrt{n}}$
        
    - The rejection region is:
        
    - **Formula:** $\{T > t_{\alpha}(n-1)\}$
        
- **Left-Tailed Test:**
    
    - Similarly, the other one-sided test is:
        
    - **Formula:** $H_0: \mu = \mu_0 \leftrightarrow H_1: \mu < \mu_0$` or `$H_0: \mu \ge \mu_0 \leftrightarrow H_1: \mu < \mu_0$
        
    - Then the rejection region is:
        
    - **Formula:** $\{T < -t_{\alpha}(n-1)\}$

***
### 1.3 Test for the variance when the mean is known

**1. Two-sided Test**

- **Hypotheses:**
    
    - The hypotheses are:
        
    - **Formula:** $H_0: \sigma^2 = \sigma_0^2 \leftrightarrow H_1: \sigma^2 \neq \sigma_0^2$
        
- **Test Statistic:**
    
    - From the maximum likelihood estimate of σ2:
        
    - **Formula:** $\hat{\sigma}^2 = \frac{1}{n}\sum_{i=1}^{n}(X_i - \mu)^2$
        
    - Construct the test statistic:
        
    - **Formula:** $\chi^2 = \frac{1}{\sigma_0^2}\sum_{i=1}^{n}(X_i - \mu)^2 = \frac{n\hat{\sigma}^2}{\sigma_0^2} \sim \chi^2(n)$
        
- **Rejection Region:**
    
    - The rejection region is:
        
    - **Formula:** $\{\chi^2 < \chi_{1-\frac{\alpha}{2}}^2(n)\} \cup \{\chi^2 > \chi_{\frac{\alpha}{2}}^2(n)\}$
        

**2. One-sided Test**

- **Right-Tailed Test:**
    
    - The hypotheses are:
        
    - **Formula:** $H_0: \sigma^2 = \sigma_0^2 \leftrightarrow H_1: \sigma^2 > \sigma_0^2$ or $H_0: \sigma^2 \le \sigma_0^2 \leftrightarrow H_1: \sigma^2 > \sigma_0^2$
        
    - The rejection region is:
        
    - **Formula:** $\{\chi^2 > \chi_{\alpha}^2(n)\}$
        
- **Left-Tailed Test:**
    
    - The other test is:
        
    - **Formula:** $H_0: \sigma^2 = \sigma_0^2 \leftrightarrow H_1: \sigma^2 < \sigma_0^2$ or $H_0: \sigma^2 \ge \sigma_0^2 \leftrightarrow H_1: \sigma^2 < \sigma_0^2$
        
    - The rejection region is:
        
    - **Formula:** $\{\chi^2 < \chi_{1-\alpha}^2(n)\}$

***
### 1.4 Test for the variance when the mean is unknown

- **Test Statistic:**
    
    - The test statistic is:
        
    - **Formula:** $\chi^2 = \frac{(n-1)S^2}{\sigma_0^2} \sim \chi^2(n-1)$
        
- **Rejection Region:**
    
    - For a two-sided test, the rejection region is:
        
    - **Formula:** $\{\chi^2 < \chi_{1-\frac{\alpha}{2}}^2(n-1)\} \cup \{\chi^2 > \chi_{\frac{\alpha}{2}}^2(n-1)\}$
        
- **One-sided Tests:**
    
    - The one-sided tests are similar to the case when the mean is known.