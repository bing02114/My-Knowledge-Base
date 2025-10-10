### 1.Chebyshev's inequality

$P\{|X-\mu| \ge \epsilon\} \le \frac{\sigma^2}{\epsilon^2}, \forall \epsilon > 0$

### 2.Bernoulli's Law of Large Numbers

$\lim_{n \to \infty} P\{|\frac{n_A}{n} - p| \ge \epsilon\} = 0$

### 3.Central Limit Theorem for i.i.d variables

Let $X_1, X_2, \dots, X_n$ be mutually independent and identically distributed, with $E(X_i) = \mu, D(X_i) = \sigma^2, i=1, 2, \dots$. Then for a sufficiently large n, we have:

$$\sum_{i=1}^{n} X_i \xrightarrow{d} N(n\mu, n\sigma^2)$$

which means:

$$\frac{X_1 + \dots + X_n - n\mu}{\sqrt{n}\sigma} \xrightarrow{d} N(0, 1)$$

which means:

$$\lim_{n \to \infty} P\left(\frac{X_1 + \dots + X_n - n\mu}{\sqrt{n}\sigma} \le x\right) = \Phi(x)$$

### 4.De Moivre-Laplace Theorem

The Binomial distribution can be approximated by the Normal distribution.

$$n_A \xrightarrow{d} N(np, np(1-p))$$

which means:

$$\frac{X_1 + \dots + X_n - np}{\sqrt{np(1-p)}} \xrightarrow{d} N(0,1)$$

which means:

$$\lim_{n \to \infty} P\left(\frac{X_1 + \dots + X_n - np}{\sqrt{np(1-p)}} \le x\right) = \Phi(x)$$