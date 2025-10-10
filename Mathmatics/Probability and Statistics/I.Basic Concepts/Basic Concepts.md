### I.Addtion Rule

**For Two Events:**

$$P(A_1 \cup A_2) = P(A_1) + P(A_2) - P(A_1 A_2)$$
**For Three Events:**

$$P(A_1 \cup A_2 \cup A_3) = P(A_1) + P(A_2) + P(A_3) - P(A_1 A_2) - P(A_1 A_3) - P(A_2 A_3) + P(A_1 A_2 A_3)$$

**General Formula / Principle of Inclusion-Exclusion**

$$P(\bigcup_{i=1}^{n} A_i) = \sum_{i=1}^{n} P(A_i) - \sum_{1 \le i < j \le n} P(A_i A_j) + \sum_{1 \le i < j < k \le n} P(A_i A_j A_k) + \dots + (-1)^{n-1} P(A_1 A_2 \dots A_n)$$


### II.Conditional Probability

**Definition**:

$$P(B|A) = \frac{P(AB)}{P(A)}$$

**Multiplication Rule**

$$P(AB) = P(B)P(A|B) = P(A)P(B|A)$$

**Chain Rule:**

$$P(A_1 A_2 \dots A_n) = P(A_1)P(A_2|A_1)P(A_3|A_1 A_2) \dots P(A_n|A_1 A_2 \dots A_{n-1})$$

### III.Law of Total Probability

**Basic Form:**

$$P(A) = P(AB) + P(A\bar{B}) = P(B)P(A|B) + P(\bar{B})P(A|\bar{B})$$

**General Form:**

$$P(B_i|A) = \frac{P(B_i)P(A|B_i)}{\sum_{j=1}^{n} P(B_j)P(A|B_j)}$$

### IV.Bayes' Theorem

**Basic Form:**

$$P(B|A) = \frac{P(B)P(A|B)}{P(B)P(A|B) + P(\bar{B})P(A|\bar{B})} = \frac{P(B)P(A|B)}{P(A)}$$

>**P(B|A): Posterior Probability**
>
>The probability of event B occuring, given that event A has occurred.
>
>It represents our updated belief about B **after considering the new evidence A**
>
>**P(A|B): Likelihood**
>
>The probability of obseving the evidence A, given that the hypothesis B is true.
>
>It quantifies **how likely the evidence is**, assuming the event has occurred
>
>**P(B): Prior Probability**
>
>The initial probability of event B occuring, before considering any new evidence.
>
>It's the **prior belief based on existing knowledge.**
>
>**P(A): Marginal Likelihood / Evidence**
>
>The total probability of observing the evidence A, regardless of event B.
>
>It acts as a **normalization constant** to ensure the posterior probability is a valid probability


**General Form:**

$$P(B_i|A) = \frac{P(B_i)P(A|B_i)}{\sum_{j=1}^{n} P(B_j)P(A|B_j)}$$

### V.Event Operations

**Distributive Laws:**

$$A(B \cup C) = AB \cup AC$$

$$A \cup BC = (A \cup B)(A \cup C)$$

**De Morgan's Laws:**

$$\overline{A \cup B} = \bar{A} \cap \bar{B}$$

$$\overline{A \cap B} = \bar{A} \cup \bar{B}$$

**Set Difference:**

$$A - B = A\bar{B}$$