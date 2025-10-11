### 1.Comparison of Means

#### 1.1 Test for $\mu_1-\mu_2$ with $\sigma^2_1,\sigma^2_2$ known

- **Two-Sided Test:**
    
    - **Hypotheses:**
        
        - **Formula:** $H_0: \mu_1 = \mu_2 \leftrightarrow H_1: \mu_1 \neq \mu_2$
            
    - **Test Statistic:**
        
        - **Formula:** $Z = \frac{\bar{X}_n - \bar{Y}_m}{\sqrt{\frac{\sigma_1^2}{n} + \frac{\sigma_2^2}{m}}} \sim N(0,1)$
            
    - **Rejection Region:**
        
        - **Formula:** $\{|Z| > z_{\frac{\alpha}{2}}\}$
            
- **One-Sided Tests:**
    
    - **Right-Tailed Test:**
        
        - **Hypotheses:**
            
            - **Formula:** $H_0: \mu_1 = \mu_2 \leftrightarrow H_1: \mu_1 > \mu_2$` or `$H_0: \mu_1 \le \mu_2 \leftrightarrow H_1: \mu_1 > \mu_2$
                
        - **Rejection Region:**
            
            - **Formula:** $\{Z > z_{\alpha}\}$
                
    - **Left-Tailed Test:**
        
        - **Hypotheses:**
            
            - **Formula:** $H_0: \mu_1 = \mu_2 \leftrightarrow H_1: \mu_1 < \mu_2$` or `$H_0: \mu_1 \ge \mu_2 \leftrightarrow H_1: \mu_1 < \mu_2$
                
        - **Rejection Region:**
            
            - **Formula:** $\{Z < -z_{\alpha}\}$

#### 1.2 Test for $\mu_1-\mu_2$ with $\sigma^2_1,\sigma^2_2$ unknown, but $\sigma^2_1,\sigma^2_2$ is known

- **Pooled Sample Variance ($S_W^2$):**
    
    - Introduce the pooled sample variance $S_w^2$:
        
    - **Formula:** $S_w^2 = \frac{(n-1)S_1^2 + (m-1)S_2^2}{n+m-2}$
        
- **Test Statistic:**
    
    - The test statistic is:
        
    - **Formula:** $T = \frac{\bar{X}_n - \bar{Y}_m}{S_w\sqrt{\frac{1}{n} + \frac{1}{m}}} \sim t(n+m-2)$
        
- **Rejection Region:**
    
    - The rejection region for a two-sided test is:
        
    - **Formula:** $\{|T| > t_{\frac{\alpha}{2}}(m+n-2)\}$

***
### 2.Hypothesis Test for Paired Data

- **Setup ($Z_i$):**
    
    - Introduce Zi​=Xi​−Yi​, then the differences Zi​ are assumed to follow Z∼N(μ,σ2).
        
- **Hypotheses:**
    
    - The test for a significant difference is transformed into a one-sample test of the mean of the differences:
        
    - **Formula:** $H_0: \mu = 0 \leftrightarrow H_1: \mu \neq 0$
        
- **Test Statistic:**
    
    - The test statistic is:
        
    - **Formula:** $T = \frac{\bar{Z}_n}{S_z/\sqrt{n}} \sim t(n-1)$
        
- **Rejection Region:**
    
    - The rejection region is:
        
    - **Formula:** $\{|T| > t_{\frac{\alpha}{2}}(n-1)\}$

***
### 3.Test for Comparison of Variances

#### 3.1 Test for $\frac{\sigma^2_1}{\sigma^2_2}$​ when the means are known

- **Two-Sided Test:**
    
    - **Hypotheses:**
        
        - **Formula:** $H_0: \sigma_1^2 = \sigma_2^2 \leftrightarrow H_1: \sigma_1^2 \neq \sigma_2^2$
            
    - **Test Statistic:**
        
        - **Formula:** $F = \frac{\frac{\sum(x_i-\mu_1)^2}{m}}{\frac{\sum(y_j-\mu_2)^2}{n}} \sim F(m, n)$
            
        - (_Note: In the formula, assume the first sample has size m and the second has size n._)
            
    - **Rejection Region:**
        
        - **Formula:** $\{F > F_{\frac{\alpha}{2}}(m, n)\} \cup \{F < \frac{1}{F_{\frac{\alpha}{2}}(n, m)}\}$
            
- **One-Sided Tests:**
    
    - **Right-Tailed Test:**
        
        - **Hypotheses:**
            
            - **Formula:** $H_0: \sigma_1^2 = \sigma_2^2 \leftrightarrow H_1: \sigma_1^2 > \sigma_2^2$` or `$H_0: \sigma_1^2 \le \sigma_2^2 \leftrightarrow H_1: \sigma_1^2 > \sigma_2^2$
                
        - **Rejection Region:**
            
            - **Formula:** $\{F > F_{\alpha}(m, n)\}$
                
    - **Left-Tailed Test:**
        
        - **Hypotheses:**
            
            - **Formula:** $H_0: \sigma_1^2 = \sigma_2^2 \leftrightarrow H_1: \sigma_1^2 < \sigma_2^2$ or $H_0: \sigma_1^2 \ge \sigma_2^2 \leftrightarrow H_1: \sigma_1^2 < \sigma_2^2$
                
        - **Rejection Region:**
            
            - **Formula:** $\{F < \frac{1}{F_{\alpha}(n, m)}\}$

#### 3.2 Test for comparison of variances when the means are unknown

- **Test Statistic:**
    
    - **EN:** The test statistic is:
        
    - **Formula:** $F = \frac{S_1^2}{S_2^2} \sim F(m-1, n-1)$
        
- **Two-Sided Rejection Region:**
    
    - The two-sided rejection region is:
        
    - **Formula:** $\{F > F_{\frac{\alpha}{2}}(m-1, n-1)\} \cup \{F < \frac{1}{F_{\frac{\alpha}{2}}(n-1, m-1)}\}$
        
- **One-Sided Rejection Region:**
    
    - The one-sided rejection regions are:
        
    - **Formulas:**
        
        - $\{F > F_{\alpha}(m, n)\}$
            
        - $\{F < \frac{1}{F_{\alpha}(n, m)}\}$
